from fastapi.testclient import TestClient
from app.main import app
from app.ai.recommender.engine import score
from app.config import settings
import pytest
client=TestClient(app)

@pytest.fixture(autouse=True)
def disable_external_services(monkeypatch):
 monkeypatch.setattr(settings,'weather_key','')
 monkeypatch.setattr(settings,'maps_key','')
 monkeypatch.setattr(settings,'llm_key','')
 monkeypatch.setattr(settings,'llm_model','')

def register(): return client.post('/api/auth/register',json={'name':'Demo User','email':'demo@example.com','password':'password123'})
def auth():
 r=register()
 token=r.json()['access_token'] if r.status_code==200 else client.post('/api/auth/login',json={'email':'demo@example.com','password':'password123'}).json()['access_token']
 return {'Authorization':'Bearer '+token}
def test_auth_and_current_user():
 h=auth(); assert client.get('/api/auth/me',headers=h).status_code==200
def test_session_check_returns_false_instead_of_unauthorized():
 assert client.get('/api/auth/session',headers={'Authorization':'Bearer invalid'}).json()=={'authenticated':False}
def test_cors_allows_vite_dev_ports():
 for origin in ('http://localhost:5173','http://localhost:5174','http://localhost:5175'):
  r=client.options('/api/auth/register',headers={'Origin':origin,'Access-Control-Request-Method':'POST'})
  assert r.status_code==200
  assert r.headers['access-control-allow-origin']==origin
def test_destinations_and_recommendations():
 assert len(client.get('/api/destinations').json())>=3
 assert len(client.get('/api/recommendations').json())>=1
def test_map_lookup_fails_gracefully_without_a_key():
 result=client.get('/api/maps/location',params={'location':'Motihari'}).json()
 assert result['available'] is False
def test_chat_always_has_a_local_fallback(monkeypatch):
 monkeypatch.setattr('app.api.routes.answer_chat',lambda *args:None)
 result=client.post('/api/ai/chat',json={'message':'What can I do in Kolkata?','language':'en'})
 assert result.status_code==200
 assert 'Kolkata' in result.json()['message']
 assert 'TourMitra' in result.json()['source']
def test_general_chat_fallback_does_not_invent_tourism_context(monkeypatch):
 monkeypatch.setattr('app.api.routes.answer_chat',lambda *args:None)
 result=client.post('/api/ai/chat',json={'message':'How are you?','language':'en'}).json()
 assert 'TourMitra AI Assistant' in result['message']
 assert result['source']=='TourMitra Assistant'
def test_budget_fallback_requests_missing_trip_details(monkeypatch):
 monkeypatch.setattr('app.api.routes.answer_chat',lambda *args:None)
 result=client.post('/api/ai/chat',json={'message':'budget around 10000','language':'en'}).json()
 assert 'destination' in result['message'].lower() or 'query' in result['message'].lower()
def test_plan_and_recalculate():
 r=client.post('/api/trips/plan',headers=auth(),json={'destination':'Kolkata','budget':10000,'days':3,'travellers':4,'traveller_type':'Family','interests':['culture','food'],'start_date':'2026-10-12','end_date':'2026-10-14','travel_type':'single'});assert r.status_code==200
 trip=r.json()
 assert trip['weather']['outdoor_suitability']=='unknown'
 refreshed=client.post('/api/itinerary/'+trip['id']+'/recalculate',headers=auth())
 assert refreshed.status_code==200
 assert refreshed.json()['id']==trip['id']
def test_trip_history_includes_solo_and_joined_group_trips():
 owner=client.post('/api/auth/register',json={'name':'History Owner','email':'history-owner@example.com','password':'password123'}).json()['access_token']
 guest=client.post('/api/auth/register',json={'name':'History Guest','email':'history-guest@example.com','password':'password123'}).json()['access_token']
 owner_headers={'Authorization':'Bearer '+owner}; guest_headers={'Authorization':'Bearer '+guest}
 solo=client.post('/api/trips/plan',headers=owner_headers,json={'destination':'Kolkata','budget':9000,'travellers':1,'interests':['culture'],'start_date':'2026-12-01','end_date':'2026-12-02','travel_type':'single'}).json()
 group=client.post('/api/trips/plan',headers=owner_headers,json={'destination':'Goa','budget':15000,'travellers':2,'interests':['food'],'start_date':'2026-12-10','end_date':'2026-12-12','travel_type':'group','current_location_city':'Kolkata'}).json()
 client.post('/api/trips/plan',headers=guest_headers,json={'destination':'Goa','budget':15000,'travellers':2,'interests':['food'],'start_date':'2026-12-10','end_date':'2026-12-12','travel_type':'group','current_location_city':'Kolkata'})
 request=client.post('/api/connections/'+client.get('/api/auth/me',headers=guest_headers).json()['id'],headers=owner_headers,params={'trip_id':group['id']})
 accepted=client.post('/api/connections/'+request.json()['id']+'/decision',headers=guest_headers,json={'action':'accept'})
 assert accepted.status_code==200
 owner_history=client.get('/api/trips/history',headers=owner_headers).json()
 guest_history=client.get('/api/trips/history',headers=guest_headers).json()
 assert {entry['trip']['id'] for entry in owner_history}>={solo['id'],group['id']}
 assert any(entry['trip']['id']==group['id'] and not entry['is_shared'] for entry in owner_history)
 assert any(entry['trip']['id']==group['id'] and entry['is_shared'] for entry in guest_history)
def test_plan_accepts_a_traveller_selected_destination():
 r=client.post('/api/trips/plan',headers=auth(),json={'destination':'Darjeeling','budget':15000,'days':2,'travellers':100,'interests':['nature'],'start_date':'2026-10-12','end_date':'2026-10-13','travel_type':'single'})
 assert r.status_code==200
 assert r.json()['destination']['name']=='Darjeeling'
 assert 'guides' not in r.json()
def test_scoring_and_weather_fallback():
 assert score({'tags':['culture'],'average_cost':1000,'rating':4.6,'hidden_gem_score':90,'crowd_score':20},10000,['culture'])[0]>0
 assert client.get('/api/weather/Kolkata').json()['source']=='Weather API not configured'

def test_group_matching_requires_exact_city_and_dates_and_hides_coordinates():
 one=client.post('/api/auth/register',json={'name':'Match One','email':'match-one@example.com','password':'password123'}).json()['access_token']
 two=client.post('/api/auth/register',json={'name':'Match Two','email':'match-two@example.com','password':'password123'}).json()['access_token']
 headers_one={'Authorization':'Bearer '+one}; headers_two={'Authorization':'Bearer '+two}
 base={'destination':'Goa','budget':15000,'travellers':1,'interests':['food'],'start_date':'2026-11-12','end_date':'2026-11-16','travel_type':'group','current_location_city':'Kolkata','current_location_latitude':22.57,'current_location_longitude':88.36}
 first=client.post('/api/trips/plan',headers=headers_one,json=base).json()
 client.post('/api/trips/plan',headers=headers_two,json={**base,'budget':14000,'current_location_city':'Kolkata','current_location_latitude':22.59,'current_location_longitude':88.31})
 client.post('/api/trips/plan',headers=headers_two,json={**base,'budget':13000,'current_location_city':'Howrah','current_location_latitude':22.59,'current_location_longitude':88.31})
 client.post('/api/trips/plan',headers=headers_two,json={**base,'destination':'Jaipur'})
 result=client.get('/api/travelers/matches',headers=headers_one,params={'trip_id':first['id']}).json()
 assert len(result['matches'])==1
 assert result['matches'][0]['match_percentage']==100
 request=client.post('/api/connections/'+result['matches'][0]['traveller']['id'],headers=headers_one,params={'trip_id':first['id']})
 assert request.status_code==200 and request.json()['status']=='pending'
 received=client.get('/api/connections/received',headers=headers_two).json()
 assert len(received)==1 and received[0]['connection']['id']==request.json()['id']
 decision=client.post('/api/connections/'+request.json()['id']+'/decision',headers=headers_two,json={'action':'accept'})
 assert decision.status_code==200 and decision.json()['status']=='accepted'
 assert decision.json()['trip_id']==first['id']
 shared_guide=client.get('/api/trips/'+first['id'],headers=headers_two)
 assert shared_guide.status_code==200 and shared_guide.json()['shared_with_group'] is True
 groups=client.get('/api/travel-groups',headers=headers_two).json()
 assert len(groups)==1 and result['matches'][0]['traveller']['id'] in groups[0]['member_ids']
 message=client.post('/api/travel-groups/'+groups[0]['id']+'/messages',headers=headers_two,json={'message':'Let us plan the trip!'})
 assert message.status_code==200
 assert client.get('/api/travel-groups/'+groups[0]['id']+'/messages',headers=headers_one).json()[0]['message']=='Let us plan the trip!'
 assert client.delete('/api/travel-groups/'+groups[0]['id'],headers=headers_one).json()=={'deleted':True}
 assert client.get('/api/travel-groups',headers=headers_one).json()==[]
 assert client.get('/api/travel-groups',headers=headers_two).json()==[]
 assert 'current_location_latitude' not in str(result)
 assert 'current_location_longitude' not in str(result)

def test_multiple_accepted_requests_join_the_same_group():
 tokens=[]
 for name,email in [('Group Owner','group-owner@example.com'),('Group Two','group-two@example.com'),('Group Three','group-three@example.com')]:
  registered=client.post('/api/auth/register',json={'name':name,'email':email,'password':'password123'})
  token=registered.json()['access_token'] if registered.status_code==200 else client.post('/api/auth/login',json={'email':email,'password':'password123'}).json()['access_token']
  tokens.append({'Authorization':'Bearer '+token})
 trip_input={'destination':'Goa','budget':15000,'travellers':1,'interests':['food'],'start_date':'2026-12-12','end_date':'2026-12-16','travel_type':'group','current_location_city':'Kolkata'}
 owner_trip=client.post('/api/trips/plan',headers=tokens[0],json=trip_input).json()
 client.post('/api/trips/plan',headers=tokens[1],json=trip_input)
 client.post('/api/trips/plan',headers=tokens[2],json=trip_input)
 matches=client.get('/api/travelers/matches',headers=tokens[0],params={'trip_id':owner_trip['id']}).json()['matches']
 assert len(matches)==2
 requests=[client.post('/api/connections/'+match['traveller']['id'],headers=tokens[0],params={'trip_id':owner_trip['id']}).json() for match in matches]
 decisions=[]
 for headers in tokens[1:]:
  received=client.get('/api/connections/received',headers=headers).json()
  decisions.append(client.post('/api/connections/'+received[-1]['connection']['id']+'/decision',headers=headers,json={'action':'accept'}).json())
 assert decisions[0]['group_id']==decisions[1]['group_id']
 groups=client.get('/api/travel-groups',headers=tokens[0]).json()
 assert len([group for group in groups if group['trip_id']==owner_trip['id']])==1
 assert len(groups[0]['member_ids'])==3
