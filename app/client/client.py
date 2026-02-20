import httpx
from typing import Any, Dict, Optional, TypeVar, Generic, List
from fastapi import HTTPException, status

# Definimos un tipo genérico para que los hijos puedan especificar su modelo de retorno
T = TypeVar("T")

class BaseExternalClient(Generic[T]):
    def __init__(self, base_url: str, timeout: float = 10.0):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    async def _request(
        self, 
        method: str, 
        endpoint: str, 
        params: Optional[Dict[str, Any]] = None, 
        data: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None
    ) -> Any:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        # Fusionar headers base con específicos de la llamada
        headers = {**(headers or {})}
        
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            try:
                response = await client.request(
                    method=method,
                    url=url,
                    headers=headers,
                    params=params,
                    json=data
                )
                response.raise_for_status()
                return response.json()
            
            except httpx.HTTPStatusError as e:
                # Log opcional aquí del error real
                detail = f"Error en API externa ({self.__class__.__name__}): {e.response.text}"
                raise HTTPException(status_code=e.response.status_code, detail=detail)
            
            except httpx.RequestError as e:
                raise HTTPException(
                    status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                    detail=f"Servicio externo no disponible: {str(e)}"
                )