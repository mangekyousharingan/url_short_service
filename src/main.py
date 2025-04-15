from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.adapters.api.url_controller import router as url_router
from src.adapters.database.models import Base
from src.core.config import settings

app = FastAPI(
    title="URL Shortener Service",
    description="A service for shortening URLs with statistics tracking",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(url_router)

@app.on_event("startup")
async def startup():
    # Create database tables
    async with settings.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
async def root() -> dict[str, str]:
    return {
        "status": "ok",
        "environment": settings.environment,
        "message": "Welcome to Project Template API",
    }
