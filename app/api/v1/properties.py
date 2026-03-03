from fastapi import APIRouter, Depends, HTTPException, status
from app.core.dependencies import get_domus_service
from fastapi.security import OAuth2PasswordBearer
from app.service.domus_service import DomusService
from app.core.config import DEBUG

router = APIRouter()

@router.get("/")
async def get_properties(
    service: DomusService = Depends(get_domus_service)
    ):
    try:
        return await service.get_available_properties()
    except Exception as e:
        detail = "Internal server error"
        if DEBUG:
            print(e)
            detail += f" ({e})"
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail)
    
@router.get("/{property_id}")
async def get_property_by_id(
    property_id: str,
    service: DomusService = Depends(get_domus_service)
    ):
    try:
        return await service.get_property_by_id(property_id)
    except Exception as e:
        detail = "Internal server error"
        if DEBUG:
            print(e)
            detail += f" ({e})"
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail)