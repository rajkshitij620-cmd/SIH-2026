# TourMitra AI

TourMitra AI is an SIH-ready tourism MVP that recommends where a traveller should go—not just what is already popular. Its USP is **AI-powered tourism demand distribution**: interests, budget, weather, estimated crowds and local opportunities are combined into explainable suggestions.

## What works

- JWT registration, login and protected saved itineraries
- AI trip planner for the Kolkata ₹10,000 / 3-day / family / culture + food demo
- Deterministic, explainable destination recommendation engine
- Context-based crowd alternative (explicitly not real-time detection)
- Local homestay, guide, restaurant and cultural experience discovery
- Weather-aware itinerary recalculation
- English/Hindi travel assistant fallback and local RAG-style retrieval endpoint
- MongoDB Atlas-ready configuration plus a no-key, no-database demo mode

## Architecture

`React + Vite + Tailwind` → `FastAPI` → `services / recommender / auth / MongoDB`

The production integration seams live in `backend/app/services`, `backend/app/ai`, and `backend/app/database`. `DEMO_MODE=true` uses clearly-labelled, local seed data so the SIH demo stays usable without keys.

## Run locally

```bash
cd backend
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

In another terminal:

```bash
cd frontend
npm install
npm run dev
```

Open the Vite URL, register any account, then plan the suggested demo trip. Run backend checks with:

```bash
cd backend && pytest
```

## Environment and MongoDB Atlas

Copy `backend/.env.example` to `backend/.env`; set `MONGODB_URI`, a strong `JWT_SECRET`, `CORS_ORIGINS`, and optional `LLM_*`, `WEATHER_API_KEY`, `MAPS_API_KEY`. Never commit real `.env` files. Set frontend `VITE_API_BASE_URL` in root `.env` for the deployed FastAPI URL.

For Atlas, create a database user and network access rule, put its SRV URI in `MONGODB_URI`, then run:

```bash
cd backend && python -m app.database.seed
```

Without Atlas, this command reports that built-in demo data is being used.

## Deployment

Deploy `frontend/` to Vercel with `VITE_API_BASE_URL=https://your-render-service.onrender.com`. Deploy `backend/` to Render using `uvicorn app.main:app --host 0.0.0.0 --port $PORT`; configure backend variables there and allow the Vercel URL via `CORS_ORIGINS`.

## Limitations and next steps

Seed listings, pricing, crowd scores and weather are demonstration estimates and are labelled accordingly. Production should connect licensed weather/maps providers, MongoDB Atlas Vector Search, authenticated LLM calls, real availability feeds, and persistent MongoDB repositories (the MVP retains its demo data in process memory when Atlas is absent).
