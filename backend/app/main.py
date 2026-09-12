from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.config import settings
from app.api.routes import api

app = FastAPI(title='TourMitra AI', version='1.0.0')

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5174",
        "https://sih-2026-three-sigma.vercel.app",
    ],
    allow_origin_regex=r'^https?://(localhost|127\.0\.0\.1)(:\d+)?$|^https://.*\.vercel\.app$',
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH", "HEAD"],
    allow_headers=["*"],
    expose_headers=["*"],
    max_age=3600,
)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    origin = request.headers.get("origin")
    headers = {
        "Access-Control-Allow-Origin": origin if origin else "*",
        "Access-Control-Allow-Headers": "*",
        "Access-Control-Allow-Methods": "*"
    }
    if origin:
        headers["Access-Control-Allow-Credentials"] = "true"
    return JSONResponse(
        status_code=500,
        content={"detail": str(exc) or "Internal Server Error"},
        headers=headers
    )


app.include_router(api)
