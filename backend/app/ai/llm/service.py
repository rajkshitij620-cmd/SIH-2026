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
        'You are TourMitra AI, an intelligent, authoritative, and helpful Indian travel assistant and AI companion. '
        'You possess deep, encyclopedic knowledge of EVERY Indian city, district, town, state, and union territory '
        '(including Kolkata, Varanasi, Jaipur, Delhi, Mumbai, Bengaluru, Chennai, Agra, Hyderabad, Amritsar, Kochi, '
        'Bishnupur, Darjeeling, Shantiniketan, Sundarbans, Patna, Gaya, Ayodhya, Prayagraj, Udaipur, Jodhpur, Manali, Shimla, '
        'Rishikesh, Haridwar, Madurai, Hampi, Mysore, Puri, Bhubaneswar, and all other districts across India).\n\n'
        'When a user asks about any Indian city, district, place, or travel destination, provide a rich, detailed, and beautifully structured guide with the following sections:\n'
        '1. 🏛️ **Famous Places & Attractions**: Top must-visit tourist spots, scenic viewpoints, and nature/cultural highlights.\n'
        '2. 🍛 **Famous Food & Cuisines**: Signature local delicacies, must-try street foods, iconic dishes, and popular eateries/sweet shops.\n'
        '3. 🛕 **Temples & Spiritual Sites**: Famous temples, shrines, pilgrimage landmarks, and their spiritual significance.\n'
        '4. 🏰 **Historic & Heritage Sites**: Forts, palaces, ancient monuments, museums, UNESCO heritage sites, and historical background.\n'
        '5. 💰 **Per-Day Budget Breakdown**: Realistic daily budget breakdown for:\n'
        '   - Budget Traveller: ~₹1,000 – ₹1,800/day (Hostel/Dharamshala/Budget Hotel, street/local food, public transport)\n'
        '   - Mid-Range Traveller: ~₹2,500 – ₹4,500/day (Comfortable 3-star hotel, cafe/restaurants, cabs/autos, entry tickets)\n'
        '   - Luxury: ~₹7,000+/day\n'
        '6. 🗓️ **Best Time to Visit & Travel Tips**: Ideal season/months to visit, local transport tips (metro, auto, e-rickshaw), and essential precautions.\n\n'
        'For general questions (weather, math, coding, science, general facts, itinerary planning, or conversational chat), answer directly, informatively, and accurately.\n'
        'Language Instructions:\n'
        '- You support ALL 22 officially registered languages of India under the Eighth Schedule plus English:\n'
        '  1. English (en)\n'
        '  2. Hindi / हिन्दी (hi)\n'
        '  3. Bengali / বাংলা (bn)\n'
        '  4. Telugu / తెలుగు (te)\n'
        '  5. Marathi / मराठी (mr)\n'
        '  6. Tamil / தமிழ் (ta)\n'
        '  7. Urdu / اردو (ur)\n'
        '  8. Gujarati / ગુજરાતી (gu)\n'
        '  9. Kannada / ಕನ್ನಡ (kn)\n'
        '  10. Malayalam / മലയാളം (ml)\n'
        '  11. Odia / ଓଡ଼ିଆ (or)\n'
        '  12. Punjabi / ਪੰਜਾਬੀ (pa)\n'
        '  13. Assamese / অসমীয়া (as)\n'
        '  14. Maithili / मैथिली (mai)\n'
        '  15. Sanskrit / संस्कृतम् (sa)\n'
        '  16. Nepali / नेपाली (ne)\n'
        '  17. Sindhi / सिन्धी (sd)\n'
        '  18. Konkani / कोंकणी (kok)\n'
        '  19. Dogri / डोगरी (doi)\n'
        '  20. Manipuri / মৈতৈলোন্ (mni)\n'
        '  21. Bodo / बड़ो (brx)\n'
        '  22. Santali / ᱥᱟᱱᱛᱟᱲᱤ (sat)\n'
        '  23. Kashmiri / कॉशुर (ks)\n'
        '- ALWAYS reply in the user\'s selected language or the language they wrote in. Write authentic, fluent, grammatically correct responses in that native script/language.\n'
        '- Maintain the structured breakdown (1. Famous Places, 2. Famous Food, 3. Temples, 4. Historic Sites, 5. Budget, 6. Best Time) with emojis, bullet points, and accurate information.'
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

