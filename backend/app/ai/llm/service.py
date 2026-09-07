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
        "STRICT ANSWERING RULES (CRITICAL):\n"
        "1. ANSWER ONLY WHAT IS ASKED (PRECISION & RELEVANCE):\n"
        "   - If the user asks about FOOD / CUISINE / DISHES / SWEETS (e.g. 'kolkata famous food', 'Lucknow khana', 'what to eat in Jaipur'):\n"
        "     Provide ONLY the iconic dishes, street foods, traditional delicacies, and famous eateries. DO NOT list places, temples, budget, weather, or itineraries.\n"
        "   - If the user asks about SIGHTSEEING / PLACES / ATTRACTIONS (e.g. 'famous places in Delhi', 'Manali sightseeing'):\n"
        "     Provide ONLY top places to visit, attractions, and heritage landmarks. DO NOT list food, budget, or weather.\n"
        "   - If the user asks about TEMPLES / SPIRITUAL SITES (e.g. 'Varanasi temples', 'Puri Jagannath mandir darshan'):\n"
        "     Provide ONLY temples, shrines, ghats, and spiritual information.\n"
        "   - If the user asks about BUDGET / EXPENSES / TRIP COST (e.g. 'Goa trip budget', 'kitna kharcha hoga'):\n"
        "     Provide ONLY the per-day / total budget breakdown (budget, mid-range, luxury).\n"
        "   - If the user asks about WEATHER / CLIMATE / MAUSAM (e.g. 'Delhi weather', 'mausam kaisa hai'):\n"
        "     Provide ONLY live weather, temperature, and climate advice.\n"
        "   - If the user asks about BEST TIME TO VISIT / SEASON (e.g. 'kab jayein', 'best time for Darjeeling'):\n"
        "     Provide ONLY the ideal travel months and seasons.\n"
        "   - ONLY when the user asks a GENERAL city query (e.g. 'tell me about Kolkata', 'Patna travel guide', 'what is famous in Indore' without specifying a single aspect), then provide the complete structured 360° guide (Places, Food, Heritage, Budget, Best Time).\n\n"
        "2. SELECTIVE WEATHER DISCLOSURE: NEVER mention weather unless the user explicitly asked about weather/mausam/temperature/rain.\n\n"
        "3. MULTILINGUAL SUPPORT: Respond naturally and fluently in the language/script requested by the user (Hindi, English, Bengali, Telugu, Marathi, Tamil, etc.). Use bullet points and clean markdown formatting."
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

