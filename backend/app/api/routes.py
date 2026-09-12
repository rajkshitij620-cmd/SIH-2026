from fastapi import APIRouter, HTTPException, Depends, Response, Header
from pymongo.errors import DuplicateKeyError
from app.schemas.core import RegisterInput, LoginInput, ResetPasswordInput, GoogleAuthInput, TripInput, ChatInput, ConnectionDecision, GroupInput, GroupMessageInput
from app.auth.security import hash_password, verify_password, password_needs_rehash, create_token, decode_token
from app.auth.dependencies import current_user
from app.database.store import store
from app.ai.recommender.engine import recommend, crowd_alternative
from app.services.planner import plan, recalculate
from app.services.weather import get_weather, get_current_weather
from app.services.maps import directions as live_directions, location_map, static_map
from app.ai.llm.service import answer_chat, configured as llm_configured
from app.ai.cities_kb import get_city_knowledge, format_city_guide, INDIAN_CITIES_KB
import re
from uuid import uuid4
from datetime import datetime

def public_profile(user):
 return {'id':user['id'],'name':user['name'],'avatar_url':user.get('avatar_url'),'bio':user.get('bio',''),'interests':user.get('interests',[]),'travel_style':user.get('travel_style','Balanced'),'is_premium':bool(user.get('is_premium',False)),'premium_tier':user.get('premium_tier','free')}

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
 uid=str(uuid4()); u={'id':uid,'name':v.name,'email':v.email.lower(),'password_hash':hash_password(v.password),'language':'en','interests':[],'avatar_url':None,'bio':'','travel_style':'Balanced','is_premium':False,'premium_tier':'free'}
 try: store.create_user(u)
 except DuplicateKeyError: raise HTTPException(409,'Email is already registered')
 return {'access_token':create_token(uid),'token_type':'bearer','user':{k:u.get(k) for k in ('id','name','email','language','interests','avatar_url','is_premium','premium_tier')}}
@api.post('/auth/login')
def login(v:LoginInput):
 u=store.user_by_email(v.email.lower())
 if not u or not verify_password(v.password,u['password_hash']): raise HTTPException(401,'Invalid email or password')
 if password_needs_rehash(u['password_hash']):
  u=store.update_user(u['id'], {'password_hash':hash_password(v.password)})
 return {'access_token':create_token(u['id']),'token_type':'bearer','user':{k:u.get(k, False if k=='is_premium' else 'free' if k=='premium_tier' else None) for k in ('id','name','email','language','interests','avatar_url','is_premium','premium_tier')}}
@api.post('/auth/reset-password')
def reset_password(v:ResetPasswordInput):
 u=store.user_by_email(v.email.lower())
 if not u: raise HTTPException(404,'No account found with this email')
 store.update_user(u['id'], {'password_hash':hash_password(v.new_password)})
 return {'access_token':create_token(u['id']),'token_type':'bearer','user':{k:u.get(k, False if k=='is_premium' else 'free' if k=='premium_tier' else None) for k in ('id','name','email','language','interests','avatar_url','is_premium','premium_tier')},'message':'Password updated successfully'}
@api.post('/auth/google')
def google_auth(v:GoogleAuthInput):
 email=v.email.lower().strip()
 u=store.user_by_email(email)
 if not u:
  uid=str(uuid4())
  u={
   'id':uid,
   'name':v.name or 'Google Explorer',
   'email':email,
   'password_hash':hash_password(str(uuid4())),
   'language':'en',
   'interests':[],
   'avatar_url':v.avatar_url or 'https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?auto=format&fit=crop&w=200&q=80',
   'bio':'Traveler via Google Account',
   'travel_style':'Balanced',
   'is_premium':False,
   'premium_tier':'free'
  }
  try: store.create_user(u)
  except DuplicateKeyError: u=store.user_by_email(email)
 else:
  if v.avatar_url and not u.get('avatar_url'):
   u=store.update_user(u['id'], {'avatar_url':v.avatar_url})
 return {'access_token':create_token(u['id']),'token_type':'bearer','user':{k:u.get(k, False if k=='is_premium' else 'free' if k=='premium_tier' else None) for k in ('id','name','email','language','interests','avatar_url','is_premium','premium_tier')}}
@api.get('/auth/me')
def me(u=Depends(current_user)): return {k:u.get(k, False if k=='is_premium' else 'free' if k=='premium_tier' else None) for k in ('id','name','email','language','interests','avatar_url','is_premium','premium_tier')}
@api.get('/auth/session')
def session(authorization:str=Header(default='')):
 if not authorization.startswith('Bearer '): return {'authenticated':False}
 try: user=store.user_by_id(decode_token(authorization[7:]))
 except HTTPException: user=None
 if not user: return {'authenticated':False}
 return {'authenticated':True,'user':{k:user.get(k, False if k=='is_premium' else 'free' if k=='premium_tier' else None) for k in ('id','name','email','language','interests','avatar_url','is_premium','premium_tier')}}
@api.get('/premium/plans')
def premium_plans():
 return {
  'plans': [
   {
    'id': 'free',
    'name': 'Free Explorer',
    'price': 0,
    'billing': 'Free Forever',
    'description': 'Ideal for solo adventures with smart AI itinerary creation',
    'badge': 'Standard',
    'features': [
     'Personalized Day-Wise AI Itinerary',
     'Famous Places & Budget Breakdown',
     'Live Weather Tracking',
     'Solo Tour Guide'
    ]
   },
   {
    'id': 'pro_monthly',
    'name': 'TourMitra Pro Monthly',
    'price': 0,
    'original_price': 199,
    'billing': '₹0 (Free Special Offer)',
    'period': 'monthly',
    'badge': 'Free Special Offer',
    'popular': True,
    'description': 'Unlock same-city TravelMate matchmaking & VIP group features for ₹0',
    'features': [
     'Same Current City to Destination TravelMate Matching',
     'AI Compatibility Score & Mutual Match Connections',
     'Dedicated Group Room Chat & Shared Live Itinerary',
     'Golden VIP 👑 Profile Crown Badge',
     'Offline PDF Travel Itinerary Download',
     'High-Priority 24/7 Safety SOS & Support'
    ]
   },
   {
    'id': 'pro_annual',
    'name': 'TourMitra Pro Annual',
    'price': 0,
    'original_price': 1499,
    'billing': '₹0 (Free Special Offer)',
    'period': 'annual',
    'badge': '100% Free VIP',
    'popular': False,
    'description': 'Full VIP access unlocked for all SIH participants & judges for ₹0',
    'features': [
     'All Pro Monthly Features Included',
     '100% Free Special Access (₹0)',
     'Verified Annual Pro 👑 Badge',
     'Unlimited Trip Replans & AI Rerouting',
     'Exclusive Live Festival & Crowd Alerts',
     'Priority Smart Emergency Response'
    ]
   }
  ]
 }
@api.post('/premium/upgrade')
def upgrade_premium(payload: dict, u=Depends(current_user)):
 plan_id = payload.get('plan_id', 'pro_monthly')
 updated = store.update_user(u['id'], {
  'is_premium': True,
  'premium_tier': plan_id,
  'premium_since': datetime.utcnow().isoformat()
 })
 if not updated:
  raise HTTPException(500, 'Failed to activate premium')
 return {
  'success': True,
  'message': 'Successfully activated TourMitra Pro membership! 👑',
  'user': {k: updated.get(k, False if k=='is_premium' else 'free' if k=='premium_tier' else None) for k in ('id', 'name', 'email', 'language', 'interests', 'avatar_url', 'is_premium', 'premium_tier')}
 }
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
    hindi = v.language == 'hi' or any(z in msg_lower for z in ['mujhe', 'karo', 'hai', 'kaise', 'batao', 'kya', 'mausam', 'kaisa', 'namaste', 'bataiye', 'prasiddh', 'khana', 'jagah'])

    tokens = set(re.findall(r'[a-zA-Z0-9_]+', msg_lower))

    # Check query intent types
    food_keywords = {'food', 'dish', 'dishes', 'khana', 'cuisine', 'cuisines', 'sweets', 'mithai', 'taste', 'specialty', 'specialties', 'specialities', 'restaurant', 'restaurants', 'eateries', 'delicacies', 'snack', 'snacks', 'chaat', 'breakfast', 'lunch', 'dinner'}
    places_keywords = {'place', 'places', 'sightseeing', 'ghoomna', 'attraction', 'attractions', 'spots', 'monuments', 'dharohar', 'heritage', 'sthal', 'tourist', 'viewpoint', 'viewpoints'}
    temple_keywords = {'mandir', 'temple', 'temples', 'spiritual', 'dharmik', 'gurudwara', 'ashram', 'ghat', 'ghats', 'aarti', 'puja', 'darshan', 'masjid', 'church'}
    budget_keywords = {'budget', 'cost', 'kharcha', 'expense', 'expenses', 'price', 'rates', 'cheap', 'expensive'}
    time_keywords = {'season', 'months', 'timing', 'timings'}
    weather_keywords = {'weather', 'temperature', 'temp', 'mausam', 'baarish', 'rain', 'rainfall', 'humidity', 'forecast', 'climate', 'garmi', 'sardi', 'taapman'}

    is_food_inquiry = bool(tokens.intersection(food_keywords)) or any(k in msg_lower for k in ['street food', 'khana peena', 'famous food', 'kya khaye', 'kya khayein'])
    is_temple_inquiry = bool(tokens.intersection(temple_keywords)) or any(k in msg_lower for k in ['famous temple', 'famous mandir', 'puja timing', 'darshan timing'])
    is_budget_inquiry = bool(tokens.intersection(budget_keywords)) or any(k in msg_lower for k in ['how much', 'kitna kharcha', 'kitna lagega', 'per day budget', 'trip cost'])
    is_best_time_inquiry = bool(tokens.intersection(time_keywords)) or any(k in msg_lower for k in ['best time', 'when to visit', 'kab jayein', 'kab jana', 'right time', 'sahi samay'])
    is_places_inquiry = bool(tokens.intersection(places_keywords)) or any(k in msg_lower for k in ['famous places', 'tourist spot', 'ghoomne ki jagah', 'kahan ghume', 'kahan ghoomein', 'places to visit'])
    is_weather_inquiry = bool(tokens.intersection(weather_keywords))

    spec_type = None
    if is_food_inquiry:
        spec_type = 'food'
    elif is_best_time_inquiry:
        spec_type = 'best_time'
    elif is_budget_inquiry:
        spec_type = 'budget'
    elif is_temple_inquiry:
        spec_type = 'temples'
    elif is_places_inquiry:
        spec_type = 'places'

    # 1. Match Indian Cities from comprehensive Knowledge Base & Destination Store
    city_kb_data = get_city_knowledge(raw_msg)
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

    # 2. Check for live weather questions strictly
    weather_info = None
    if is_weather_inquiry:
        city_candidate = None
        if city_kb_data:
            city_candidate = city_kb_data['name']
        if not city_candidate:
            for d in matched_destinations or destinations:
                if d['name'].lower() in msg_lower:
                    city_candidate = d['name']
                    break
        if not city_candidate:
            for c in INDIAN_CITIES_KB.keys():
                if c in msg_lower:
                    city_candidate = INDIAN_CITIES_KB[c]['name']
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
    if city_kb_data:
        context_payload.append({
            'type': 'city_intelligence',
            'name': city_kb_data['name'],
            'state': city_kb_data['state'],
            'description': city_kb_data['description'],
            'famous_places': city_kb_data['famous_places'],
            'famous_food': city_kb_data['famous_food'],
            'temples_spiritual': city_kb_data['temples_spiritual'],
            'heritage_sites': city_kb_data['heritage_sites'],
            'budget': city_kb_data['budget'],
            'best_time': city_kb_data['best_time'],
            'specialties': city_kb_data['specialties'],
            'user_intent': spec_type or 'general_overview'
        })
    elif matched_destinations:
        context_payload.extend([
            {
                'type': 'destination_info',
                'name': d['name'],
                'description': d.get('description'),
                'categories': d.get('categories'),
                'average_cost': d.get('average_cost'),
                'tags': d.get('tags'),
                'famous_places': d.get('famous_places'),
                'user_intent': spec_type or 'general_overview'
            }
            for d in matched_destinations
        ])
    if is_weather_inquiry and weather_info:
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

    # 5. Smart Deterministic Fallbacks
    # A. If user asked specifically for weather and we have weather info:
    if is_weather_inquiry and weather_info:
        loc = weather_info.get('location')
        temp = weather_info.get('temperature_c')
        cond = weather_info.get('condition')
        hum = weather_info.get('humidity')
        wind = weather_info.get('wind_speed_kmh')
        if hindi:
            msg_text = f"📍 **{loc} Live Weather Report**\n\n• **Taapman**: {temp}°C (Sthiti: {cond})\n• **Aadarta (Humidity)**: {hum}%\n• **Hawa ki Gati**: {wind} km/h\n\n🌤️ *Travel Tip*: Mausam ke anusaar apne kapde aur itinerary plan karein."
        else:
            msg_text = f"📍 **{loc} Live Weather Report**\n\n• **Current Temperature**: {temp}°C ({cond})\n• **Humidity**: {hum}%\n• **Wind Speed**: {wind} km/h\n\n🌤️ *Travel Advice*: Plan your day and outdoor activities considering the current weather conditions."
        return {'message': msg_text, 'language': 'hi' if hindi else 'en', 'source': 'Live OpenWeather Service'}

    # B. If user asked greeting:
    greeting = any(term in msg_lower for term in ('hello', 'hi', 'hey', 'how are you', 'kaise ho', 'namaste', 'pranam'))
    if greeting and len(msg_lower.split()) <= 4:
        text = 'Namaste! Main TourMitra AI Assistant hoon. Main Bharat ke kisi bhi sheher ke prasiddh sthal, famous khana, mandir/dharohar, budget, aur mausam ki jaankari de sakta hoon. Aap kis sheher ke baare me jaanna chahte hain?' if hindi else 'Hello! I am TourMitra AI Assistant. I can help you with famous places, iconic foods, spiritual & heritage landmarks, budgets, itineraries, and live weather for any city in India. Which city or destination would you like to explore?'
        return {'message': text, 'language': 'hi' if hindi else 'en', 'source': 'TourMitra Assistant'}

    # C. If City Knowledge Base matched:
    if city_kb_data:
        text = format_city_guide(city_kb_data, hindi=hindi, specific_type=spec_type)
        return {'message': text, 'language': 'hi' if hindi else 'en', 'source': 'TourMitra City Intelligence'}

    # D. If Destination Store matched:
    if matched_destinations:
        d = matched_destinations[0]
        places = ', '.join(d.get('famous_places', [])) or d['name']
        cost = d.get('average_cost', 1500)
        categories = ', '.join(d.get('categories', ['Heritage', 'Sightseeing']))

        if spec_type == 'food':
            if hindi:
                text = (
                    f"🍛 **{d['name']} ke Prasiddh Vyanjan & Food Guide**\n\n"
                    f"{d['name']} apne lazeez regional khane aur street food ke liye jana jata hai.\n\n"
                    f"• Traditional regional thali & iconic local dishes\n"
                    f"• Authentic street food stalls and famous local sweets\n"
                    f"• Local snacks & tea culture\n\n"
                    f"Kya aapko {d['name']} ke specific restaurants ya food streets ke baare me jaanna hai?"
                )
            else:
                text = (
                    f"🍛 **Famous Food & Cuisines in {d['name']}**\n\n"
                    f"{d['name']} is famous for its signature traditional cuisines and vibrant street food:\n\n"
                    f"• Authentic regional delicacies & traditional thali meals\n"
                    f"• Signature local street foods and sweets\n"
                    f"• Popular food lanes and heritage tea stalls\n\n"
                    f"Let me know if you would like iconic eatery recommendations in {d['name']}!"
                )
        elif spec_type == 'places':
            if hindi:
                text = (
                    f"🏛️ **{d['name']} ke Pramukh Paryatan Sthal (Famous Places)**\n\n"
                    f"{d.get('description', '')}\n\n"
                    f"**Must-Visit Attractions:**\n"
                    f"{chr(10).join(['• ' + p for p in d.get('famous_places', [d['name']])])}\n\n"
                    f"Kya aapko {d['name']} ka day-wise sightseeing plan chahiye?"
                )
            else:
                text = (
                    f"🏛️ **Top Attractions & Sightseeing in {d['name']}**\n\n"
                    f"{d.get('description', '')}\n\n"
                    f"**Must-Visit Attractions:**\n"
                    f"{chr(10).join(['• ' + p for p in d.get('famous_places', [d['name']])])}\n\n"
                    f"Would you like a day-by-day customized itinerary for {d['name']}?"
                )
        elif spec_type == 'budget':
            if hindi:
                text = (
                    f"💰 **{d['name']} Trip Budget Breakdown (Per Day Per Person)**\n\n"
                    f"• **Budget Traveller**: ~₹{cost} – ₹{cost + 500}/din (Dharamshala/Hostel + Local Transport + Street Food)\n"
                    f"• **Mid-Range Traveller**: ~₹{cost * 2} – ₹{cost * 3}/din (Hotel + Restaurants + Auto/Cabs)\n"
                    f"• **Luxury Traveller**: ~₹{cost * 4}+/din (Resorts + Private Cabs + Fine Dining)"
                )
            else:
                text = (
                    f"💰 **Estimated Per-Day Budget Breakdown for {d['name']}**\n\n"
                    f"• **Budget Traveller**: ~₹{cost} – ₹{cost + 500}/day (Budget stay + Local transport + Meals)\n"
                    f"• **Mid-Range Traveller**: ~₹{cost * 2} – ₹{cost * 3}/day (Hotel + Restaurants + Cabs)\n"
                    f"• **Luxury Traveller**: ~₹{cost * 4}+/day (Luxury stays + Private tours + Fine dining)"
                )
        elif spec_type == 'best_time':
            btime = ', '.join(d.get('best_time', ['October to March']))
            if hindi:
                text = f"🗓️ **{d['name']} Ghoomne Ka Sahi Samay**: {btime}.\n\nIss dauran mausam suhana aur sightseeing ke liye anukool hota hai."
            else:
                text = f"🗓️ **Best Time to Visit {d['name']}**: {btime}.\n\nDuring this period, the weather is pleasant and ideal for sightseeing."
        else:
            if hindi:
                text = (
                    f"🌟 **{d['name']} Travel Guide**\n\n"
                    f"{d.get('description', '')}\n\n"
                    f"1. 🏛️ **Prasiddh Paryatan Sthal (Famous Places)**: {places}\n"
                    f"2. 🍛 **Prasiddh Khana (Famous Food)**: Local authentic street food, traditional sweets & regional cuisine\n"
                    f"3. 🛕 **Dharmik & Dharohar Sthal (Heritage & Temples)**: {categories} historical monuments, ancient shrines & scenic attractions\n"
                    f"4. 💰 **Per-Day Budget Breakdown**:\n"
                    f"   • Budget: ~₹{cost} – ₹{cost + 500}/din (Stay + Local Food + Transport)\n"
                    f"   • Mid-Range: ~₹{cost * 2} – ₹{cost * 3}/din (Hotel + Restaurants + Cabs)\n"
                    f"5. 🗓️ **Ghoomne Ka Sabse Accha Samay**: October se March\n\n"
                    f"Kya aapko {d['name']} ka day-wise itinerary ya hotel guide chahiye?"
                )
            else:
                text = (
                    f"🌟 **{d['name']} Travel Guide**\n\n"
                    f"{d.get('description', '')}\n\n"
                    f"1. 🏛️ **Famous Places & Must-Visit Attractions**: {places}\n"
                    f"2. 🍛 **Famous Food & Signature Delicacies**: Iconic local dishes, street food & regional sweets\n"
                    f"3. 🛕 **Temples & Heritage Landmarks**: {categories} monuments and cultural heritage sites\n"
                    f"4. 💰 **Estimated Per-Day Budget Breakdown**:\n"
                    f"   • Budget Traveller: ~₹{cost} – ₹{cost + 500}/day\n"
                    f"   • Mid-Range Traveller: ~₹{cost * 2} – ₹{cost * 3}/day\n"
                    f"5. 🗓️ **Best Time to Visit**: October to March for pleasant sightseeing weather.\n\n"
                    f"Let me know if you would like a detailed day-wise itinerary for {d['name']}!"
                )
        return {'message': text, 'language': 'hi' if hindi else 'en', 'source': 'TourMitra Knowledge Base'}

    # E. General Fallback query
    if hindi:
        text = f"Aapka sawaal mila: '{raw_msg}'. Main Bharat ke kisi bhi sheher ke prasiddh sthal (famous places), local food, mandir/dharohar, budget aur mausam (weather) ke baare me poori jaankari de sakta hoon. Kripya sheher ka naam ya apna specific sawal batayein!"
    else:
        text = f"Received your query: '{raw_msg}'. I can help you discover top attractions, famous cuisines, spiritual/heritage monuments, budgets, and live weather for any Indian destination. Please mention a city name or your specific travel question!"
    return {'message': text, 'language': 'hi' if hindi else 'en', 'source': 'TourMitra Assistant'}
@api.post('/ai/rag/search')
def rag(v:ChatInput): return {'results':[x for x in store.destinations() if any(w in (x['description']+' '+' '.join(x['tags'])).lower() for w in v.message.lower().split())][:3],'source':'Local fallback retrieval'}
