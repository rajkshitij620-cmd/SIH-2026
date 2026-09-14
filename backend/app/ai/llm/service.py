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
        "You are TourMitra AI, an intelligent, authoritative, and world-class Indian travel & tourism AI companion.\n\n"
        "CORE CAPABILITIES & INSTRUCTIONS:\n"
        "You provide comprehensive, rich, authentic, and beautifully structured travel intelligence for ANY city, town, hill station, spiritual center, heritage site, or village across India (both small and large destinations).\n\n"
        "COMPREHENSIVE CITY & TOURIST PLACE GUIDE FORMAT:\n"
        "Whenever a user asks about any city, town, or tourist place in India (e.g. 'Dehradun', 'Varanasi', 'tell me about Patna', 'Manali guide', 'what is in Almora', etc.), provide a thorough, complete 360° guide covering ALL the following key aspects with clean markdown and emojis:\n\n"
        "1. 🌟 **Overview & Essence**: Brief introduction to the place, geography/state, historical background, and vibe.\n"
        "2. 🏛️ **Top Sightseeing & Famous Places**: Key landmarks, viewpoints, forts, monuments, and must-visit attractions.\n"
        "3. 🛕 **Temples & Spiritual Sites**: Famous mandirs, ghats, ancient shrines, gurudwaras, churches, or monasteries with spiritual importance.\n"
        "4. 🌳 **Parks, Gardens & Nature Spots**: Scenic parks, lakes, waterfalls, botanical gardens, wildlife/bird sanctuaries, and peaceful outdoor locations.\n"
        "5. 🍲 **Famous Food & Iconic Eateries**: Signature local dishes, authentic street foods, famous sweets, and legendary food streets or iconic shops.\n"
        "6. 🏨 **Hotels & Stay Recommendations**: Best neighborhoods/areas to stay, with suggestions across Budget (dharamshalas/hostels), Mid-range family hotels, and Luxury resorts.\n"
        "7. 🗓️ **Best Time to Visit & Ideal Duration**: Optimal travel months, weather/season highlights, and recommended number of days to explore.\n"
        "8. 🚗 **How to Reach & Local Transport**: Nearest airport, major railway junction, highway road connectivity, and local transit options (metro, e-rickshaws, cabs, auto, scooter rental).\n"
        "9. 💰 **Estimated Budget Breakdown**: Per-day approximate budget (Budget: ₹1,000–1,500/day, Mid-range: ₹2,500–4,000/day, Luxury: ₹6,000+/day).\n"
        "10. 🛍️ **Shopping & Local Specialties**: Famous handicrafts, handlooms, souvenirs, and traditional markets.\n\n"
        "SPECIFIC INQUIRIES:\n"
        "- If the user specifically asks about only one or two categories (e.g. 'best hotels in Jaipur' or 'street food in Indore' or 'temples in Ujjain'), give an exceptionally detailed, deep-dive response for that specific topic first, and then provide a helpful brief list of complementary highlights and travel tips.\n\n"
        "MULTILINGUAL & FORMATTING RULES:\n"
        "- Respond in the exact language/script of the user's query (Hindi, Hinglish, English, Bengali, Tamil, Telugu, Marathi, Gujarati, etc.).\n"
        "- When replying in Hindi or Hinglish, use fluent, natural, polite, and warm conversational tone.\n"
        "- Use bullet points, bold text, and clean formatting for maximum readability."
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

