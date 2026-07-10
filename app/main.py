from fastapi import FastAPI

from app.api.routes import router
from app.config.settings import settings

app = FastAPI(
    title=settings.APP_NAME,
    description="AI-powered platform for complaint analysis and intelligent routing.",
    version=settings.APP_VERSION,
)

app.include_router(router)