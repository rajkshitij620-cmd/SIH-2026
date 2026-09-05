import httpx
from datetime import date
from app.config import settings

def _fallback(location, visit_date=None, source='Weather API not configured', notice=None):
    return {
        'location': location,
        'condition': 'Weather forecast unavailable',
        'temperature_c': None,
        'outdoor_suitability': 'unknown',
        'source': source,
        'forecast_date': visit_date.isoformat() if visit_date else None,
        'notice': notice or 'Add a weather API key to receive weather-based indoor or outdoor recommendations for this visit date.',
    }

def get_weather(location, visit_date=None):
    visit_date=visit_date or date.today()
    if not settings.weather_key:
        return _fallback(location,visit_date)
    try:
        response=httpx.get('https://api.openweathermap.org/data/2.5/forecast',params={'q':location,'appid':settings.weather_key,'units':'metric'},timeout=6)
        response.raise_for_status()
        data=response.json()
        forecast=next((item for item in data['list'] if item.get('dt_txt','').startswith(visit_date.isoformat())),None)
        if not forecast:
            return _fallback(location, visit_date, 'Forecast unavailable for this date', 'OpenWeather provides a limited forecast window. Choose a date within the next five days and try again.')
        condition=forecast['weather'][0]['description'].title()
        temperature=round(forecast['main']['temp'])
        weather_group=forecast['weather'][0]['main'].lower()
        outdoor='low' if weather_group in {'thunderstorm','drizzle','rain','snow','tornado'} else 'medium' if weather_group in {'mist','fog','haze','smoke'} else 'high'
        return {'location':data.get('city',{}).get('name',location),'condition':condition,'temperature_c':temperature,'outdoor_suitability':outdoor,'source':'OpenWeather date forecast','forecast_date':visit_date.isoformat(),'notice':'Forecasts are most reliable close to the visit date; check again before travel.'}
    except httpx.HTTPStatusError as error:
        status = error.response.status_code
        if status in {401, 403}:
            return _fallback(location, visit_date, 'Weather API authentication failed', 'Your OpenWeather key was rejected. Check that WEATHER_API_KEY is active and belongs to an account with 5-day forecast access.')
        if status == 429:
            return _fallback(location, visit_date, 'Weather API rate limit reached', 'Too many weather requests were made. Please wait a few minutes and recalculate the itinerary.')
        return _fallback(location, visit_date, 'Weather API temporarily unavailable', f'OpenWeather returned HTTP {status}. Please try again shortly.')
    except (httpx.HTTPError, KeyError, IndexError, TypeError, ValueError):
        return _fallback(location, visit_date, 'Weather API temporarily unavailable', 'The weather service could not be reached. Check your internet connection and try again.')

def get_current_weather(location: str) -> dict:
    if not settings.weather_key:
        return {'location': location, 'condition': 'Pleasant', 'temperature_c': 27, 'humidity': 65, 'wind_speed_kmh': 10, 'success': False}
    try:
        response = httpx.get(
            'https://api.openweathermap.org/data/2.5/weather',
            params={'q': location, 'appid': settings.weather_key, 'units': 'metric'},
            timeout=6
        )
        response.raise_for_status()
        data = response.json()
        condition = data['weather'][0]['description'].title() if data.get('weather') else 'Clear'
        temperature = round(data.get('main', {}).get('temp', 25))
        feels_like = round(data.get('main', {}).get('feels_like', temperature))
        humidity = data.get('main', {}).get('humidity', 60)
        wind_speed = round(data.get('wind', {}).get('speed', 3.0) * 3.6, 1)
        city_name = data.get('name', location)
        return {
            'location': city_name,
            'condition': condition,
            'temperature_c': temperature,
            'feels_like_c': feels_like,
            'humidity': humidity,
            'wind_speed_kmh': wind_speed,
            'success': True
        }
    except Exception:
        return {'location': location, 'condition': 'Pleasant / Clear', 'temperature_c': 28, 'humidity': 60, 'wind_speed_kmh': 12, 'success': False}
