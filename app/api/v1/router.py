from fastapi import APIRouter
from app.api.v1 import properties

router = APIRouter()

@router.get("/")
def root():
    return {"status": "ok", "message": "API working 🚀"}

router.include_router(properties.router, prefix="/domus", tags=["Domus"])