from fastapi import APIRouter
from app.api.v1 import properties

router = APIRouter()

router.include_router(properties.router, prefix="/domus", tags=["Domus"])