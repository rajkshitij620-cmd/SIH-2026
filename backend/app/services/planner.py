from uuid import uuid4
from datetime import date, timedelta, datetime
from app.ai.recommender.engine import recommend, crowd_alternative
from app.services.weather import get_weather
from app.database.demo_data import BUSINESSES
from app.database.store import store
from app.ai.llm.service import generate_itinerary_narrative, configured as llm_configured
from app.schemas.core import TripInput

def _options(destination, category, maximum):
    return [x for x in BUSINESSES if x['category']==category and x['location'].lower()==destination.lower() and x['price']<=maximum]

def plan(payload, user_id=None, persist=True):
    ranked=recommend(payload.budget,payload.interests)
    requested=payload.destination.strip()
    base=next((x for x in ranked if x['name'].lower()==requested.lower()),None)
    custom=base is None
    start_date=date.fromisoformat(payload.start_date)
    trip_days=(date.fromisoformat(payload.end_date)-start_date).days+1
    visit_dates=[start_date+timedelta(days=index) for index in range(trip_days)]
    if custom:
        title_dest=requested.title()
        base={'id':f'custom-{uuid4()}','name':title_dest,'location':{'city':title_dest,'state':'India'},'description':f'Explore the vibrant culture, local heritage and attractions of {title_dest}.','categories':['culture','heritage','food'],'rating':4.6,'average_cost':round(payload.budget/trip_days),'crowd_score':50,'hidden_gem_score':65,'tags':payload.interests,'activities':[f'{title_dest} Heritage Trail',f'{title_dest} Local Market Walk'],'famous_places':[f'{title_dest} Historic Landmark',f'{title_dest} Central Gardens & Promenade',f'{title_dest} Old City Heritage Walk',f'{title_dest} Cultural Arts Complex',f'{title_dest} Local Bazaar',f'{title_dest} Sunset Point'],'indoor_places':[f'{title_dest} Heritage Museum & Gallery',f'{title_dest} Arts & Crafts Pavilion'],'outdoor_places':[f'{title_dest} Botanical Gardens & Lake',f'{title_dest} Landmark Viewpoint'],'best_time':['October–March']}
    daily_weather=[get_weather(base['name'],visit_date) for visit_date in visit_dates]
    weather=daily_weather[0]
    daily_budget=payload.budget/trip_days
    stay_budget_per_night=payload.budget*.35/trip_days
    stays=sorted(_options(base['name'],'Homestay',stay_budget_per_night),key=lambda x:(-x['rating'],x['price']))
    if not stays:
        stays=[{'id':f'stay-{uuid4()}','name':f'{base["name"]} Heritage Homestay','category':'Homestay','location':base['name'],'price':max(900,round(stay_budget_per_night*0.85)),'rating':4.6,'description':f'Comfortable homestay centrally located in {base["name"]}.','verified':True}]
    restaurants=_options(base['name'],'Restaurant',daily_budget*.25)
    if not restaurants:
        restaurants=[{'id':f'rest-{uuid4()}','name':f'{base["name"]} Local Dining & Traditional Kitchen','category':'Restaurant','location':base['name'],'price':max(250,round(daily_budget*0.2)),'rating':4.7,'description':f'Authentic local cuisine and regional specialties in {base["name"]}.','verified':True}]
    experiences=_options(base['name'],'Cultural Experience',daily_budget*.2)
    if not experiences:
        experiences=[{'id':f'exp-{uuid4()}','name':f'{base["name"]} Guided Heritage & Culture Trail','category':'Cultural Experience','location':base['name'],'price':max(200,round(daily_budget*0.15)),'rating':4.8,'description':f'Explore the historic lanes and artisan traditions of {base["name"]}.','verified':True}]
    days=[]
    all_famous=base.get('famous_places') or []
    indoor_places=base.get('indoor_places') or []
    outdoor_places=base.get('outdoor_places') or []
    places_per_day=max(1,(len(all_famous)+trip_days-1)//trip_days) if all_famous else 0

    for index in range(trip_days):
        day_weather=daily_weather[index]
        rainy=day_weather['outdoor_suitability']=='low'
        if all_famous:
            day_famous=[all_famous[(index*places_per_day+offset)%len(all_famous)] for offset in range(min(places_per_day,len(all_famous)))]
        else:
            day_famous=[f'{base["name"]} Landmark {index+1}']
        first_place=(indoor_places[index%len(indoor_places)] if indoor_places else f'{base["name"]} Heritage Museum') if rainy else (day_famous[0] if day_famous else f'{base["name"]} Central Landmark')
        second_place=(indoor_places[(index+1)%len(indoor_places)] if indoor_places else f'{base["name"]} Arts Gallery') if rainy else (day_famous[1] if len(day_famous)>1 else (experience['name'] if experiences else f'{base["name"]} Sunset Promenade'))
        stay=stays[index%len(stays)] if stays else None
        restaurant=restaurants[index%len(restaurants)] if restaurants else None
        experience=experiences[index%len(experiences)] if experiences else None
        local_options=[option for option in (experience,) if option]
        days.append({'day':index+1,'date':visit_dates[index].isoformat(),'theme':'Indoor discovery' if rainy else 'Outdoor highlights','weather':day_weather,'famous_places':day_famous,'local_options':local_options,'activities':[{'time':'09:30 AM','place':first_place,'category':'Indoor discovery' if rainy else 'Heritage & Sightseeing','estimated_cost':0,'travel_time':'15-25 mins','crowd':'Moderate morning flow','weather':day_weather['condition'],'why_recommended':'Rain-safe indoor cultural visit.' if rainy else f"Must-visit famous attraction scheduled for Day {index+1}."},{'time':'01:00 PM','place':restaurant['name'],'category':'Food','estimated_cost':restaurant['price'],'travel_time':'10-15 mins','crowd':'Lunch hours','weather':day_weather['condition'],'why_recommended':'Authentic local cuisine within your daily budget.'},{'time':'04:30 PM','place':second_place,'category':'Indoor activity' if rainy else 'Sightseeing & Evening Leisure','estimated_cost':experience['price'] if (experience and second_place==experience['name']) else 0,'travel_time':'20 mins','crowd':'Evening leisure','weather':day_weather['condition'],'why_recommended':'Rain-safe cultural experience.' if rainy else f"Famous evening spot organized for Day {index+1}."}]})
    rainy=weather['outdoor_suitability']=='low'
    alternative=crowd_alternative(base['id'],payload.budget,payload.interests) if not custom else {'popular_destination':base,'alternative':None,'notice':'No crowd comparison is available for this destination.'}
    travel_guide={'famous_places':base['famous_places'],'best_time':base['best_time'],'weather_advice':'Rain is expected, so parks and open walks were replaced with indoor places.' if rainy else 'Conditions support outdoor highlights; recheck weather before leaving.','local_transportation':'Use verified local taxis, public transport, or app-based rides; confirm the fare before starting a trip.','safety_tips':['Keep emergency contacts and booking details offline.','Use licensed transport and keep valuables secure in crowded areas.','Share your day plan with someone you trust.'],'stay_budget_per_night':round(stay_budget_per_night),'best_stay':stays[0] if stays else None,'stays':stays,'restaurants':restaurants,'notice':None if not custom else 'For a custom destination, live attraction, stay, and restaurant listings need a connected provider.'}
    context={'trip_request':payload.model_dump(),'destination':base,'weather':weather,'recommendation_guide':travel_guide,'verified_activity_schedule':days}
    narrative=generate_itinerary_narrative(context)
    if narrative:
        for index, day in enumerate(days): day['theme']=narrative.day_themes[index]
    trip_input={**payload.model_dump(), 'days': trip_days, 'destination': requested.title(), 'current_location_city': payload.current_location_city.title() if payload.current_location_city else None}
    result={'id':str(uuid4()),'created_at':datetime.utcnow().isoformat(),'destination':base,'days':days,'input':trip_input,'weather':weather,'weather_by_date':daily_weather,'crowd_alternative':alternative,'recommendations':ranked[:3],'travel_guide':travel_guide,'budget_breakdown':{'accommodation':min(payload.budget*.35,trip_days*1800),'food':min(payload.budget*.22,trip_days*900),'travel':min(payload.budget*.15,trip_days*500),'experiences':min(payload.budget*.18,trip_days*950)},'weather_update_message':'Your itinerary was updated for rain: indoor places were prioritised.' if rainy else None,'ai_summary':narrative.summary if narrative else None,'ai_recommendation_reason':narrative.recommendation_reason if narrative else None,'llm_enabled':llm_configured(),'source':'Destination guide generated from supplied trip details and verified demo listings.'}
    if persist:
        store.save_itinerary({**result,'user_id':user_id,'saved':False})
    return result

def recalculate(identifier):
    existing=store.itinerary_by_id(identifier)
    if not existing:
        return None
    refreshed=plan(TripInput(**existing['input']), existing['user_id'], persist=False)
    refreshed.update({'id':identifier,'user_id':existing['user_id'],'saved':existing.get('saved',False)})
    return store.update_itinerary(identifier, refreshed)
