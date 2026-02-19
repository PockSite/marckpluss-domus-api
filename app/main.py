from fastapi import FastAPI
from app.api.v1.router import router
from app.core.config import ENV



app = FastAPI()

app.include_router(router, prefix="/api/v1")
