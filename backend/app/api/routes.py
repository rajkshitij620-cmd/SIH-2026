from fastapi import APIRouter, HTTPException, Depends, Response, Header
from pymongo.errors import DuplicateKeyError
from app.schemas.core import RegisterInput, LoginInput, ResetPasswordInput, TripInput, ChatInput, ConnectionDecision, GroupInput, GroupMessageInput
from app.auth.security import hash_password, verify_password, password_needs_rehash, create_token, decode_token
from app.auth.dependencies import current_user
from app.database.store import store
from app.ai.recommender.engine import recommend, crowd_alternative
from app.services.planner import plan, recalculate
from app.services.weather import get_weather, get_current_weather
from app.services.maps import directions as live_directions, location_map, static_map
from app.ai.llm.service import answer_chat, configured as llm_configured
from uuid import uuid4
from datetime import datetime

def public_profile(user):
 return {'id':user['id'],'name':user['name'],'avatar_url':user.get('avatar_url'),'bio':user.get('bio',''),'interests':user.get('interests',[]),'travel_style':user.get('travel_style','Balanced')}

def safe_trip(trip):
 """Never expose another traveller's precise location."""
 return {'id':trip['id'],'destination':trip['destination']['name'],'start_date':trip['input']['start_date'],'end_date':trip['input']['end_date'],'budget':trip['input']['budget'],'travel_type':trip['input']['travel_type'],'gender':trip['input'].get('gender'),'age':trip['input'].get('age'),'connection_option':trip['input'].get('connection_option'),'current_location_city':trip['input'].get('current_location_city'),'trip_photo':trip['input'].get('trip_photo')}

def matching_enabled(trip):
 """Group trips remain matchable for existing API clients; new UI matching is opt-in."""
 return trip['input'].get('travel_type')=='group' or trip['input'].get('connection_option')=='connect_people'

def budget_score(own, other):
 difference=abs(own-other)/own*100
 return 20 if difference<=10 else 15 if difference<=20 else 10 if difference<=35 else 5

api=APIRouter(prefix='/api')
@api.get('/health')
def health(): return {'status':'ok','mode':'mongodb' if store.mongo is not None else 'demo','llm_configured':llm_configured()}
@api.post('/auth/register')
def register(v:RegisterInput):
 if store.user_by_email(v.email.lower()): raise HTTPException(409,'Email is already registered')
 uid=str(uuid4()); u={'id':uid,'name':v.name,'email':v.email.lower(),'password_hash':hash_password(v.password),'language':'en','interests':[],'avatar_url':None,'bio':'','travel_style':'Balanced'}
 try: store.create_user(u)
 except DuplicateKeyError: raise HTTPException(409,'Email is already registered')
 return {'access_token':create_token(uid),'token_type':'bearer','user':{k:u[k] for k in ('id','name','email','language','interests','avatar_url')}}
@api.post('/auth/login')
def login(v:LoginInput):
 u=store.user_by_email(v.email.lower())
 if not u or not verify_password(v.password,u['password_hash']): raise HTTPException(401,'Invalid email or password')
 if password_needs_rehash(u['password_hash']):
  u=store.update_user(u['id'], {'password_hash':hash_password(v.password)})
 return {'access_token':create_token(u['id']),'token_type':'bearer','user':{k:u.get(k) for k in ('id','name','email','language','interests','avatar_url')}}
@api.post('/auth/reset-password')
def reset_password(v:ResetPasswordInput):
 u=store.user_by_email(v.email.lower())
 if not u: raise HTTPException(404,'No account found with this email')
 store.update_user(u['id'], {'password_hash':hash_password(v.new_password)})
 return {'access_token':create_token(u['id']),'token_type':'bearer','user':{k:u.get(k) for k in ('id','name','email','language','interests','avatar_url')},'message':'Password updated successfully'}
@api.get('/auth/me')
def me(u=Depends(current_user)): return {k:u.get(k) for k in ('id','name','email','language','interests','avatar_url')}
@api.get('/auth/session')
def session(authorization:str=Header(default='')):
 if not authorization.startswith('Bearer '): return {'authenticated':False}
 try: user=store.user_by_id(decode_token(authorization[7:]))
 except HTTPException: user=None
 if not user: return {'authenticated':False}
 return {'authenticated':True,'user':{k:user[k] for k in ('id','name','email','language','interests')}}
@api.get('/destinations')
def destinations(q:str=''):
 data=store.destinations(); return [x for x in data if q.lower() in (x['name']+' '+x['description']+' '+' '.join(x['tags'])).lower()]
@api.get('/destinations/search')
def search(q:str=''): return destinations(q)
@api.get('/destinations/nearby')
def nearby(): return store.destinations()[1:]
@api.get('/destinations/{identifier}')
def destination(identifier:str):
 x=next((x for x in store.destinations() if x['id']==identifier),None)
 if not x: raise HTTPException(404,'Destination not found')
 return x
@api.get('/recommendations')
def recommendations(budget:int=10000, interests:str='culture,food'): return recommend(budget,interests.split(','))
@api.get('/recommendations/crowd-alternative')
def alternative(destination:str='kolkata',budget:int=10000,interests:str='culture,food'): return crowd_alternative(destination,budget,interests.split(','))
@api.get('/businesses')
def businesses(category:str=''): return [x for x in store.businesses() if not category or x['category'].lower()==category.lower()]
@api.get('/hotels')
def hotels(): return businesses('Homestay')
@api.get('/experiences')
def experiences(): return businesses('Cultural Experience')
@api.get('/weather/{location}')
def weather(location): return get_weather(location)
@api.get('/maps/directions')
def directions(origin:str='', destination:str=''):
 result=live_directions(origin,destination)
 if not result: raise HTTPException(503,'Live map lookup is unavailable. Check MAPS_API_KEY and the place names.')
 return result
@api.get('/maps/location')
def map_location(location:str):
 result=location_map(location)
 if not result:
  return {'available':False,'notice':'Live map preview is unavailable. Add a valid MAPS_API_KEY to backend/.env and restart the backend.'}
 return {**result,'available':True,'source':'MapTiler live geocoding'}
@api.get('/maps/static')
def map_static(location:str):
 result=static_map(location)
 if not result: raise HTTPException(503,'Live map preview is unavailable. Check MAPS_API_KEY and the place name.')
 content,content_type=result
 return Response(content=content,media_type=content_type,headers={'Cache-Control':'public, max-age=900'})
@api.post('/trips/plan')
def trip(v:TripInput,u=Depends(current_user)): return plan(v,u['id'])
@api.get('/trips/history')
def trip_history(u=Depends(current_user)):
 groups=store.groups_for_user(u['id'])
 groups_by_trip={group['trip_id']:group for group in groups}
 entries=[]
 seen_trip_ids=set()
 for trip in store.itineraries_for_user(u['id']):
  group=groups_by_trip.get(trip['id'])
  entries.append({'trip':trip,'group':group,'is_shared':False})
  seen_trip_ids.add(trip['id'])
 for group in groups:
  if group['trip_id'] in seen_trip_ids: continue
  trip=store.itinerary_by_id(group['trip_id'])
  if trip:
   entries.append({'trip':trip,'group':group,'is_shared':True})
   seen_trip_ids.add(trip['id'])
 return sorted(entries,key=lambda entry:(entry['trip'].get('created_at',''),entry['trip']['input'].get('start_date','')),reverse=True)
@api.get('/trips/saved')
def saved_tours(u=Depends(current_user)):
 groups=store.groups_for_user(u['id'])
 groups_by_trip={group['trip_id']:group for group in groups}
 entries=[]
 seen_trip_ids=set()
 for trip in store.itineraries_for_user(u['id']):
  if not trip.get('saved'): continue
  entries.append({'trip':trip,'group':groups_by_trip.get(trip['id']),'is_shared':False})
  seen_trip_ids.add(trip['id'])
 for group in groups:
  if group['trip_id'] in seen_trip_ids: continue
  trip=store.itinerary_by_id(group['trip_id'])
  if trip and trip.get('saved'):
   entries.append({'trip':trip,'group':group,'is_shared':True})
   seen_trip_ids.add(trip['id'])
 return sorted(entries,key=lambda entry:(entry['trip'].get('created_at',''),entry['trip']['input'].get('start_date','')),reverse=True)
@api.get('/trips/{identifier}')
def trip_get(identifier:str,u=Depends(current_user)):
 x=store.itinerary_by_id(identifier)
 if not x: raise HTTPException(404,'Trip not found')
 owner=x['user_id']==u['id']
 shared=any(group['trip_id']==identifier and u['id'] in group['member_ids'] for group in store.groups_for_user(u['id']))
 if not owner and not shared: raise HTTPException(404,'Trip not found')
 return {**x,'shared_with_group':shared and not owner}
@api.post('/trips/{identifier}/save')
def save(identifier:str,u=Depends(current_user)):
 x=store.itinerary_by_id(identifier)
 shared=any(group['trip_id']==identifier and u['id'] in group['member_ids'] for group in store.groups_for_user(u['id']))
 if not x or (x['user_id']!=u['id'] and not shared): raise HTTPException(404,'Trip not found')
 return store.update_itinerary(identifier, {'saved': True})
@api.delete('/trips/{identifier}')
def delete(identifier:str,u=Depends(current_user)):
 x=store.itinerary_by_id(identifier)
 if not x: raise HTTPException(404,'Trip not found')
 if x['user_id']==u['id']:
  store.delete_itinerary(identifier)
  for group in store.groups_for_user(u['id']):
   if group['trip_id']==identifier: store.delete_group(group['id'])
  return {'deleted':True}
 groups=store.groups_for_user(u['id'])
 removed=False
 for group in groups:
  if group['trip_id']==identifier and u['id'] in group['member_ids']:
   new_members=[m for m in group['member_ids'] if m!=u['id']]
   if new_members: store.update_group(group['id'], {'member_ids': new_members})
   else: store.delete_group(group['id'])
   removed=True
 if not removed: raise HTTPException(404,'Trip not found')
 return {'deleted':True}
@api.get('/trips')
def trips(u=Depends(current_user)): return store.saved_itineraries(u['id'])
@api.post('/itinerary/{identifier}/recalculate')
def recalc(identifier:str,u=Depends(current_user)):
 x=recalculate(identifier)
 if not x or x['user_id']!=u['id']: raise HTTPException(404,'Trip not found')
 return x
@api.get('/travelers/matches')
def traveler_matches(trip_id:str='',destination:str='',u=Depends(current_user)):
 user_trips=store.itineraries_for_user(u['id'])
 if not trip_id and user_trips:
  for t in reversed(user_trips):
   if matching_enabled(t): trip_id=t['id']; break
  if not trip_id: trip_id=user_trips[-1]['id']
 if trip_id:
  own=store.itinerary_by_id(trip_id)
  if not own or own['user_id']!=u['id']: raise HTTPException(404,'Trip not found')
  city=own['input'].get('current_location_city') or ''
  candidates=store.group_trips(own['destination']['name'],own['input']['start_date'],own['input']['end_date'],city,u['id']) if city else []
  matches=[]
  for candidate in candidates:
   other=store.user_by_id(candidate['user_id'])
   if not other: continue
   score=80+budget_score(own['input']['budget'],candidate['input']['budget'])
   connection=store.connection(u['id'],other['id'])
   c_status='accepted' if connection and connection.get('status')=='accepted' else 'pending' if connection and connection.get('status')=='pending' and connection.get('sender_id')==u['id'] else 'received' if connection and connection.get('status')=='pending' and connection.get('receiver_id')==u['id'] else None
   profile=public_profile(other); profile['avatar_url']=candidate['input'].get('trip_photo') or profile['avatar_url']
   matches.append({'traveller':profile,'trip':safe_trip(candidate),'match_percentage':score,'budget_difference_percentage':round(abs(own['input']['budget']-candidate['input']['budget'])/own['input']['budget']*100,1),'connection_status':c_status})
  matches.sort(key=lambda x:(-x['match_percentage'],x['budget_difference_percentage']))
  matched_ids={m['trip']['id'] for m in matches}
  dest_candidates=store.all_matchable_trips(exclude_user_id=u['id'],destination=own['destination']['name'])
  same_dest=[]
  for candidate in dest_candidates:
   if candidate['id'] in matched_ids: continue
   other=store.user_by_id(candidate['user_id'])
   if not other: continue
   connection=store.connection(u['id'],other['id'])
   c_status='accepted' if connection and connection.get('status')=='accepted' else 'pending' if connection and connection.get('status')=='pending' and connection.get('sender_id')==u['id'] else 'received' if connection and connection.get('status')=='pending' and connection.get('receiver_id')==u['id'] else None
   profile=public_profile(other); profile['avatar_url']=candidate['input'].get('trip_photo') or profile['avatar_url']
   same_dest.append({'traveller':profile,'trip':safe_trip(candidate),'connection_status':c_status})
  return {'trip':safe_trip(own),'user_trips':[safe_trip(t) for t in user_trips],'matches':matches,'same_destination_travelers':same_dest,'notice':'Only travellers with compatible destination details are shown.'}
 all_candidates=store.all_matchable_trips(exclude_user_id=u['id'],destination=destination if destination else None)
 travelers=[]
 for candidate in all_candidates:
  other=store.user_by_id(candidate['user_id'])
  if not other: continue
  connection=store.connection(u['id'],other['id'])
  c_status='accepted' if connection and connection.get('status')=='accepted' else 'pending' if connection and connection.get('status')=='pending' and connection.get('sender_id')==u['id'] else 'received' if connection and connection.get('status')=='pending' and connection.get('receiver_id')==u['id'] else None
  profile=public_profile(other); profile['avatar_url']=candidate['input'].get('trip_photo') or profile['avatar_url']
  travelers.append({'traveller':profile,'trip':safe_trip(candidate),'connection_status':c_status})
 return {'trip':None,'user_trips':[],'matches':[],'same_destination_travelers':travelers,'notice':'Explore travellers heading to destinations across India.'}
@api.get('/travelers/{identifier}/public-profile')
def traveller_public_profile(identifier:str,trip_id:str='',u=Depends(current_user)):
 traveller=store.user_by_id(identifier)
 if not traveller: raise HTTPException(404,'Traveller not found')
 result={'profile':public_profile(traveller)}
 if trip_id:
  own=store.itinerary_by_id(trip_id)
  connected=any(connection['trip_id']==trip_id and u['id'] in (connection['sender_id'],connection['receiver_id']) for connection in store.received_connections(u['id']))
  if not own or (own['user_id']!=u['id'] and not connected): raise HTTPException(404,'Trip not found')
  candidate=own if own['user_id']==identifier else next((x for x in store.group_trips(own['destination']['name'],own['input']['start_date'],own['input']['end_date'],own['input'].get('current_location_city',''),u['id']) if x['user_id']==identifier),None)
  if not candidate:
   candidate=own if own['user_id']==identifier else next((x for x in store.all_matchable_trips(exclude_user_id=u['id'],destination=own['destination']['name']) if x['user_id']==identifier),None)
  if candidate:
   result['profile']['avatar_url']=candidate['input'].get('trip_photo') or result['profile']['avatar_url']
   result.update({'trip':safe_trip(candidate),'match_percentage':80+budget_score(own['input']['budget'],candidate['input']['budget'])})
 return result
@api.post('/connections/{traveller_id}')
def send_connection(traveller_id:str,trip_id:str='',u=Depends(current_user)):
 if traveller_id==u['id']: raise HTTPException(400,'You cannot connect with yourself')
 if not store.user_by_id(traveller_id): raise HTTPException(404,'Traveller not found')
 own=store.itinerary_by_id(trip_id) if trip_id else None
 if not own:
  user_trips=store.itineraries_for_user(u['id'])
  if user_trips: own=user_trips[-1]; trip_id=own['id']
  else: raise HTTPException(400,'Please plan a trip first before connecting with TravelMates')
 existing=store.connection(u['id'],traveller_id)
 if existing:
  if existing.get('status')=='declined':
   return store.update_connection(existing['id'],{'status':'pending','sender_id':u['id'],'receiver_id':traveller_id,'trip_id':trip_id,'created_at':datetime.utcnow().isoformat()})
  return existing
 return store.save_connection({'id':str(uuid4()),'sender_id':u['id'],'receiver_id':traveller_id,'trip_id':trip_id,'status':'pending','created_at':datetime.utcnow().isoformat()})
@api.post('/connections/{identifier}/decision')
def decide_connection(identifier:str,v:ConnectionDecision,u=Depends(current_user)):
 connection=store.connection_by_id(identifier)
 if not connection or connection['receiver_id']!=u['id']: raise HTTPException(404,'Connection request not found')
 was_pending=connection['status']=='pending'
 updated=store.update_connection(identifier,{'status':'accepted' if v.action=='accept' else 'declined'})
 if v.action=='accept' and was_pending:
  trip=store.itinerary_by_id(connection.get('trip_id') or '')
  if not trip:
   sender_trips=store.itineraries_for_user(connection['sender_id'])
   trip=sender_trips[-1] if sender_trips else None
  dest_name=trip['destination']['name'] if (trip and trip.get('destination')) else 'Travel'
  s_date=trip['input']['start_date'] if (trip and trip.get('input')) else ''
  e_date=trip['input']['end_date'] if (trip and trip.get('input')) else ''
  trip_identifier=trip['id'] if trip else (connection.get('trip_id') or str(uuid4()))
  group=store.group_for_trip_with_member(trip_identifier,connection['sender_id']) if trip_identifier else None
  if not group:
   for g in store.groups_for_user(u['id']):
    if connection['sender_id'] in g.get('member_ids',[]):
     group=g; break
  if group:
   group=store.update_group(group['id'],{'member_ids':list(dict.fromkeys([*group['member_ids'],connection['receiver_id'],connection['sender_id']]))})
  else:
   group=store.save_group({'id':str(uuid4()),'name':f"{dest_name} Travel Group",'trip_id':trip_identifier,'destination':dest_name,'start_date':s_date,'end_date':e_date,'member_ids':[connection['sender_id'],connection['receiver_id']],'created_at':datetime.utcnow().isoformat()})
  updated['group_id']=group['id']; updated['trip_id']=trip_identifier
 return updated
@api.get('/connections/received')
def received_connections(u=Depends(current_user)):
 requests=[]
 for connection in store.received_connections(u['id']):
  sender=store.user_by_id(connection['sender_id'])
  if not sender: continue
  trip=store.itinerary_by_id(connection.get('trip_id') or '')
  if not trip:
   sender_trips=store.itineraries_for_user(sender['id'])
   trip=sender_trips[-1] if sender_trips else None
  profile=public_profile(sender)
  if trip:
   profile['avatar_url']=trip['input'].get('trip_photo') or profile['avatar_url']
   trip_data=safe_trip(trip)
  else:
   trip_data={'id':'','destination':'Destination','start_date':'','end_date':'','budget':0,'travel_type':'single','gender':None,'age':None,'current_location_city':None,'trip_photo':None}
  requests.append({'connection':connection,'traveller':profile,'trip':trip_data})
 return requests
@api.get('/travel-groups')
def travel_groups(u=Depends(current_user)):
 return store.groups_for_user(u['id'])
@api.get('/travel-groups/{identifier}/messages')
def group_messages(identifier:str,u=Depends(current_user)):
 group=store.group_by_id(identifier)
 if not group or u['id'] not in group['member_ids']: raise HTTPException(404,'Travel group not found')
 return [{'id':message['id'],'message':message['message'],'created_at':message['created_at'],'sender':public_profile(store.user_by_id(message['sender_id']))} for message in store.group_messages_for(identifier)]
@api.delete('/travel-groups/{identifier}')
def end_travel_group(identifier:str,u=Depends(current_user)):
 group=store.group_by_id(identifier)
 if not group or u['id'] not in group['member_ids']: raise HTTPException(404,'Travel group not found')
 store.delete_group(identifier)
 return {'deleted':True}
@api.post('/travel-groups/{identifier}/messages')
def send_group_message(identifier:str,v:GroupMessageInput,u=Depends(current_user)):
 group=store.group_by_id(identifier)
 if not group or u['id'] not in group['member_ids']: raise HTTPException(404,'Travel group not found')
 return store.save_group_message({'id':str(uuid4()),'group_id':identifier,'sender_id':u['id'],'message':v.message.strip(),'created_at':datetime.utcnow().isoformat()})
@api.post('/travel-groups')
def create_group(v:GroupInput,u=Depends(current_user)):
 trip=store.itinerary_by_id(v.trip_id)
 if not trip or trip['user_id']!=u['id']: raise HTTPException(404,'Trip not found')
 members=list(dict.fromkeys([u['id'],*v.member_ids]))
 for member in members[1:]:
  connection=store.connection(u['id'],member)
  if not connection or connection['status']!='accepted': raise HTTPException(400,'Groups can include accepted TravelMates only')
 return store.save_group({'id':str(uuid4()),'name':v.name,'trip_id':v.trip_id,'destination':trip['destination']['name'],'start_date':trip['input']['start_date'],'end_date':trip['input']['end_date'],'member_ids':members,'created_at':datetime.utcnow().isoformat()})
@api.post('/ai/chat')
def chat(v: ChatInput):
    raw_msg = v.message.strip()
    msg_lower = raw_msg.lower()
    hindi = v.language == 'hi' or any(z in msg_lower for z in ['mujhe', 'karo', 'hai', 'kaise', 'batao', 'kya', 'mausam', 'kaisa', 'namaste', 'bataiye'])

    # 1. Destination context
    destinations = store.destinations()
    matched_destinations = [
        x for x in destinations
        if x['name'].lower() in msg_lower
    ]
    if not matched_destinations:
        stop_words = {'a', 'an', 'the', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'about', 'around', 'what', 'can', 'i', 'do', 'how', 'is', 'are', 'you', 'me', 'my', 'budget', 'trip', 'plan', 'travel', 'tell', 'give', 'show', 'batao', 'kya', 'hai', 'kaise', 'karo', 'mujhe', 'where', 'when', 'want'}
        query_words = [w.strip('?,.! ') for w in msg_lower.split() if len(w.strip('?,.! ')) > 3 and w.strip('?,.! ') not in stop_words]
        matched_destinations = [
            x for x in destinations
            if any(qw in [t.lower() for t in x.get('tags', [])] or qw in x['name'].lower().split() for qw in query_words)
        ][:3]

    # 2. Check for live weather questions
    weather_keywords = {'weather', 'temperature', 'temp', 'mausam', 'baarish', 'rain', 'humidity', 'forecast', 'climate', 'garmi', 'sardi'}
    is_weather_inquiry = any(k in msg_lower for k in weather_keywords)
    weather_info = None
    if is_weather_inquiry:
        city_candidate = None
        for d in destinations:
            if d['name'].lower() in msg_lower:
                city_candidate = d['name']
                break
        if not city_candidate:
            common_cities = ['kolkata', 'mumbai', 'delhi', 'bangalore', 'bengaluru', 'chennai', 'hyderabad', 'jaipur', 'goa', 'darjeeling', 'pune', 'ahmedabad', 'lucknow', 'varanasi', 'manali', 'shimla', 'agra', 'sundarbans', 'shantiniketan', 'bishnupur', 'digha', 'puri']
            for c in common_cities:
                if c in msg_lower:
                    city_candidate = c.title()
                    break
        if not city_candidate:
            for prep in ['in ', 'of ', 'ka ', 'ke ']:
                if prep in msg_lower:
                    part = msg_lower.split(prep)[-1].strip().split()[0].strip('?,.! ')
                    if len(part) > 2:
                        city_candidate = part.title()
                        break
        if city_candidate:
            weather_data = get_current_weather(city_candidate)
            if weather_data and weather_data.get('temperature_c') is not None:
                weather_info = weather_data

    # 3. Context for LLM
    context_payload = []
    if matched_destinations:
        context_payload.extend([
            {
                'type': 'destination_info',
                'name': d['name'],
                'description': d.get('description'),
                'categories': d.get('categories'),
                'average_cost': d.get('average_cost'),
                'tags': d.get('tags'),
                'famous_places': d.get('famous_places')
            }
            for d in matched_destinations
        ])
    if weather_info:
        context_payload.append({
            'type': 'live_weather',
            'city': weather_info.get('location'),
            'condition': weather_info.get('condition'),
            'temperature_c': weather_info.get('temperature_c'),
            'feels_like_c': weather_info.get('feels_like_c'),
            'humidity': weather_info.get('humidity'),
            'wind_speed_kmh': weather_info.get('wind_speed_kmh')
        })

    # 4. Attempt Live LLM Answer
    target_lang = v.language or ('hi' if hindi else 'en')
    live_answer = answer_chat(raw_msg, target_lang, context_payload if context_payload else None)
    if live_answer:
        return {'message': live_answer, 'language': target_lang, 'source': 'TourMitra AI Assistant'}

    # 5. Smart Fallbacks
    if weather_info:
        loc = weather_info.get('location')
        temp = weather_info.get('temperature_c')
        cond = weather_info.get('condition')
        hum = weather_info.get('humidity')
        wind = weather_info.get('wind_speed_kmh')
        if hindi:
            msg_text = f"📍 {loc} ka live mausam: Taapman {temp}°C hai, sthiti '{cond}' hai. Humidity {hum}% aur hawa ki gati {wind} km/h hai."
        else:
            msg_text = f"📍 Live Weather in {loc}: Currently {temp}°C with {cond}. Humidity is at {hum}%, and wind speed is {wind} km/h."
        return {'message': msg_text, 'language': 'hi' if hindi else 'en', 'source': 'Live OpenWeather service'}

    greeting = any(term in msg_lower for term in ('hello', 'hi', 'hey', 'how are you', 'kaise ho', 'namaste'))
    if greeting:
        text = 'Namaste! Main TourMitra AI Assistant hoon. Main aapki travel planning, weather updates, sightseeing, aur kisi bhi generic sawaal me madad kar sakta hoon. Aap kya jaanna chahte hain?' if hindi else 'Hello! I am TourMitra AI Assistant. I can assist you with travel planning, live weather, attractions, culture, and any questions you have. How can I help you today?'
        return {'message': text, 'language': 'hi' if hindi else 'en', 'source': 'TourMitra Assistant'}

    if matched_destinations:
        d = matched_destinations[0]
        places = ', '.join(d.get('famous_places', [])) or d['name']
        cost = d.get('average_cost', 1500)
        categories = ', '.join(d.get('categories', ['Heritage', 'Sightseeing']))
        if hindi:
            text = (
                f"🌟 **{d['name']} Travel Guide**\n\n"
                f"{d.get('description', '')}\n\n"
                f"1. 🏛️ **Famous Places**: {places}\n"
                f"2. 🍛 **Famous Food**: Local street food, traditional regional thali & sweets\n"
                f"3. 🛕 **Temples & Spiritual Sites**: Famous local temples and sacred heritage spots\n"
                f"4. 🏰 **Historic & Heritage**: {categories} monuments and cultural landmarks\n"
                f"5. 💰 **Per-Day Budget**:\n"
                f"   - Budget: ~₹{cost} – ₹{cost + 500}/day\n"
                f"   - Mid-Range: ~₹{cost * 2} – ₹{cost * 3}/day\n"
                f"6. 🗓️ **Best Time to Visit**: October se March tak ghoomne ke liye sabse accha samay hai.\n\n"
                f"Agar aapko day-wise complete itinerary ya hotel planning chahiye toh batayein!"
            )
        else:
            text = (
                f"🌟 **{d['name']} Travel Guide**\n\n"
                f"{d.get('description', '')}\n\n"
                f"1. 🏛️ **Famous Places & Attractions**: {places}\n"
                f"2. 🍛 **Famous Food & Cuisines**: Iconic local dishes, street food & regional sweets\n"
                f"3. 🛕 **Temples & Spiritual Sites**: Historical temples, shrines and sacred sites\n"
                f"4. 🏰 **Historic & Heritage Sites**: {categories} monuments and heritage attractions\n"
                f"5. 💰 **Per-Day Budget Breakdown**:\n"
                f"   - Budget Traveller: ~₹{cost} – ₹{cost + 500}/day (Stay + Local Food + Transport)\n"
                f"   - Mid-Range: ~₹{cost * 2} – ₹{cost * 3}/day (Hotel + Restaurants + Cabs)\n"
                f"6. 🗓️ **Best Time to Visit**: October to March for pleasant weather.\n\n"
                f"Let me know if you would like a detailed day-wise itinerary!"
            )
        return {'message': text, 'language': 'hi' if hindi else 'en', 'source': 'TourMitra Knowledge Base'}

    if hindi:
        text = f"Aapka sawaal mila: '{raw_msg}'. Main travel destinations, live weather updates, itineraries, aur general knowledge ke sabhi sawaalon me aapki poori madad kar sakta hoon. Kripya apna specific requirement batayein!"
    else:
        text = f"Received your query: '{raw_msg}'. I am here to help you with destination recommendations, real-time weather forecasts, day-wise itineraries, and general knowledge questions. How would you like to proceed?"
    return {'message': text, 'language': 'hi' if hindi else 'en', 'source': 'TourMitra Assistant'}
@api.post('/ai/rag/search')
def rag(v:ChatInput): return {'results':[x for x in store.destinations() if any(w in (x['description']+' '+' '.join(x['tags'])).lower() for w in v.message.lower().split())][:3],'source':'Local fallback retrieval'}
