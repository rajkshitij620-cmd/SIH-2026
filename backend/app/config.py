import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[1] / '.env')

class Settings:
    mongodb_uri = os.getenv('MONGODB_URI', '')
    database_name = os.getenv('DATABASE_NAME', 'tourmitra')
    jwt_secret = os.getenv('JWT_SECRET', 'demo-only-change-in-production')
    jwt_algorithm = os.getenv('JWT_ALGORITHM', 'HS256')
    access_minutes = int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES', '1440'))
    cors_origins = [
        origin.strip().rstrip('/')
        for origin in os.getenv(
            'CORS_ORIGINS',
            'http://localhost:5173,http://localhost:5174',
        ).split(',')
        if origin.strip()
    ]
    # Local Vite can choose the next free port (for example 5173, 5174, or
    # 5175).  Keep production origins explicit via CORS_ORIGINS while making
    # local development resilient to that port change.
    cors_origin_regex = os.getenv(
        'CORS_ORIGIN_REGEX',
        r'^https?://(localhost|127\.0\.0\.1)(:\d+)?$',
    )
    demo_mode = os.getenv('DEMO_MODE', 'true').lower() == 'true'
    weather_key = os.getenv('WEATHER_API_KEY', '')
    maps_key = os.getenv('MAPS_API_KEY', '')
    llm_key = os.getenv('LLM_API_KEY', '')
    llm_model = os.getenv('LLM_MODEL', '')
    llm_base_url = os.getenv('LLM_BASE_URL', 'https://api.openai.com/v1')

settings = Settings()
