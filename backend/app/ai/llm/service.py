"""OpenAI-compatible LLM service with safe, deterministic fallbacks.

No tourism facts are sourced from the model: it receives curated context and is
only allowed to enrich that context with itinerary summaries and explanations.
"""
import json
import logging
from typing import Any, Optional
from pydantic import BaseModel, Field, ValidationError
from app.config import settings

logger = logging.getLogger(__name__)

class ItineraryNarrative(BaseModel):
    summary: str = Field(min_length=10, max_length=700)
    recommendation_reason: str = Field(min_length=10, max_length=500)
    day_themes: list[str] = Field(min_length=1, max_length=14)

def configured() -> bool:
    return bool(settings.llm_key and settings.llm_model)

def _client():
    from openai import OpenAI
    return OpenAI(api_key=settings.llm_key, base_url=settings.llm_base_url, timeout=8.0, max_retries=0)

def _completion(instructions: str, user_context: dict[str, Any], schema: Optional[dict] = None) -> str:
    """Works with OpenAI and providers implementing Chat Completions."""
    client = _client()
    request = {
        'model': settings.llm_model,
        'temperature': 0.2,
        'messages': [
            {'role': 'system', 'content': instructions},
            {'role': 'user', 'content': json.dumps(user_context, ensure_ascii=False)},
        ],
    }
    if schema:
        request['response_format'] = {
            'type': 'json_schema',
            'json_schema': {'name': 'tourmitra_itinerary', 'strict': True, 'schema': schema},
        }
    response = client.chat.completions.create(**request)
    return response.choices[0].message.content or ''

def generate_itinerary_narrative(context: dict[str, Any]) -> Optional[ItineraryNarrative]:
    if not configured():
        return None
    schema = {
        'type': 'object', 'additionalProperties': False,
        'properties': {
            'summary': {'type': 'string'},
            'recommendation_reason': {'type': 'string'},
            'day_themes': {'type': 'array', 'items': {'type': 'string'}},
        },
        'required': ['summary', 'recommendation_reason', 'day_themes'],
    }
    instructions = (
        'You are TourMitra AI, a responsible Indian tourism assistant. '
        'Create concise itinerary narrative JSON only. Use exclusively the supplied facts. '
        'Never invent venues, prices, live weather, availability, travel times, or crowd data. '
        'Keep day_themes equal in count to trip_request.days. Mention estimates as estimates.'
    )
    try:
        parsed = ItineraryNarrative.model_validate_json(_completion(instructions, context, schema))
        if len(parsed.day_themes) != context['trip_request']['days']:
            raise ValueError('Invalid number of itinerary days')
        return parsed
    except Exception as exc:
        logger.warning('LLM itinerary fallback used: %s', type(exc).__name__)
        return None

def answer_chat(message: str, language: str, tourism_context: Optional[list[dict]] = None) -> Optional[str]:
    if not configured():
        return None
    system_prompt = (
        "You are TourMitra AI, an intelligent, authoritative, and specialized Indian travel & tourism AI companion.\n\n"
        "CORE INSTRUCTIONS:\n"
        "1. STRICT RELEVANCE: Directly answer the user's question with a focus on Travel, Tourism, Heritage, Culture, Food, Itineraries, Budgets, and Weather (when requested).\n"
        "2. SELECTIVE WEATHER DISCLOSURE: ONLY include current weather, temperature, or forecasts when the user EXPLICITLY asks about weather (keywords like weather, temperature, mausam, rain, climate, baarish, forecast). If the user does NOT ask for weather, DO NOT provide weather information.\n"
        "3. INDIAN CITIES & FAMOUS THINGS:\n"
        "   When a user asks about ANY Indian city, district, town, or state (e.g. 'tell me about Patna', 'Varanasi famous things', 'Lucknow food', 'Jaipur sightseeing', 'what is famous in Indore', etc.), provide an authentic, high-quality, comprehensive guide structured with:\n"
        "   - 🏛️ **Famous Places & Must-Visit Attractions**: Top landmarks, scenic viewpoints, historical monuments, and sightseeing highlights.\n"
        "   - 🍛 **Famous Food & Local Delicacies**: Signature authentic dishes, iconic street foods, sweets, and famous food streets or eateries.\n"
        "   - 🛕 **Temples & Spiritual / Heritage Sites**: Renowned temples, shrines, forts, palaces, and cultural background.\n"
        "   - 💰 **Estimated Per-Day Budget Breakdown**:\n"
        "     • Budget Traveller: ~₹1,000 – ₹1,800/day (Dharamshala/Hostel, local eateries, public transport)\n"
        "     • Mid-Range Traveller: ~₹2,500 – ₹4,500/day (3-star hotel, cafes/restaurants, auto/cabs, entry tickets)\n"
        "     • Luxury: ~₹6,000+/day (4-5 star heritage stays, fine dining, private tours)\n"
        "   - 🗓️ **Best Time to Visit & Local Commute Tips**: Ideal months/season to visit and best transport options (metro, e-rickshaw, cabs).\n"
        "4. TARGETED SPECIFIC QUERIES:\n"
        "   - If user asks only about food -> Detail signature dishes, street food spots, and authentic sweets.\n"
        "   - If user asks only about weather -> Provide live conditions, temperature, humidity, and packing/travel tips for that weather.\n"
        "   - If user asks for an itinerary -> Provide a day-by-day sightseeing plan.\n"
        "5. MULTILINGUAL & MULTI-SCRIPT SUPPORT:\n"
        "   - Support all 22 scheduled Indian languages (Hindi, Bengali, Telugu, Marathi, Tamil, Urdu, Gujarati, Kannada, Malayalam, Odia, Punjabi, Assamese, Maithili, Sanskrit, etc.) and English.\n"
        "   - ALWAYS respond fluently and naturally in the language requested or written by the user. Use emojis, clear headings, and clean bullet points for readability."
    )
    models_to_try = [settings.llm_model, 'gpt-4o-mini', 'gpt-4o', 'gpt-3.5-turbo']
    models_to_try = list(dict.fromkeys([m for m in models_to_try if m]))
    client = _client()
    context_str = json.dumps(tourism_context, ensure_ascii=False) if tourism_context else ''
    messages = [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': f"Question: {message}\nLanguage: {language}" + (f"\nContext: {context_str}" if context_str else "")}
    ]
    for model_name in models_to_try:
        try:
            response = client.chat.completions.create(
                model=model_name,
                messages=messages,
                temperature=0.3,
                max_tokens=1500,
                timeout=18.0
            )
            content = response.choices[0].message.content
            if content and content.strip():
                return content.strip()
        except Exception as exc:
            logger.warning('LLM chat model %s error: %s', model_name, exc)
            continue
    return None

