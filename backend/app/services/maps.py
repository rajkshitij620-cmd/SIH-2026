import math
from urllib.parse import quote
import httpx
from app.config import settings

MAPTILER_BASE='https://api.maptiler.com'

def _geocode(place):
    if not settings.maps_key or not place.strip():
        return None
    response=httpx.get(f'{MAPTILER_BASE}/geocoding/{quote(place.strip(), safe="")}.json',params={'key':settings.maps_key,'limit':1},timeout=6)
    response.raise_for_status()
    features=response.json().get('features',[])
    if not features:
        return None
    feature=features[0]
    longitude,latitude=feature['center']
    return {'label':feature.get('place_name',place),'longitude':longitude,'latitude':latitude}

def location_map(place):
    try:
        return _geocode(place)
    except (httpx.HTTPError, KeyError, IndexError, TypeError, ValueError):
        return None

def static_map(place):
    point=location_map(place)
    if not point:
        return None
    url=f'{MAPTILER_BASE}/maps/streets-v2/static/{point["longitude"]},{point["latitude"]},11/800x420.png'
    try:
        response=httpx.get(url,params={'key':settings.maps_key},timeout=10)
        response.raise_for_status()
        return response.content, response.headers.get('content-type','image/png')
    except httpx.HTTPError:
        return None

def directions(origin, destination):
    start=location_map(origin)
    end=location_map(destination)
    if not start or not end:
        return None
    latitude_delta=math.radians(end['latitude']-start['latitude'])
    longitude_delta=math.radians(end['longitude']-start['longitude'])
    a=math.sin(latitude_delta/2)**2+math.cos(math.radians(start['latitude']))*math.cos(math.radians(end['latitude']))*math.sin(longitude_delta/2)**2
    distance_km=round(6371*2*math.asin(math.sqrt(a)),1)
    return {'origin':start,'destination':end,'distance_km':distance_km,'source':'MapTiler live geocoding','notice':'Distance is a straight-line estimate; turn-by-turn routing is not included in MapTiler Cloud.'}
