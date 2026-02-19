from fastapi import APIRouter, Depends, HTTPException, status
from app.core.dependencies import get_domus_service, get_user_service
from fastapi.security import OAuth2PasswordBearer
from app.service.domus_service import DomusService
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

router = APIRouter()

@router.get("/")
def get_users(service: DomusService = Depends(get_domus_service)):
    return service.get_available_properties()