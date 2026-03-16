from app.client.client import BaseExternalClient
from app.core.config import DOMUS_API_KEY, DOMUS_URL

class DomusClient(BaseExternalClient[dict]):
    def __init__(self, timeout = 10):
        super().__init__(DOMUS_URL, timeout)

    async def get_all_properties(self, inmobiliaria_id: int = 1, per_page: int = 300) -> list:
        # Ajustamos los headers exactos que Domus espera
        headers = {
            "inmobiliaria": str(inmobiliaria_id),
            "perpage": str(per_page),
            "Authorization": DOMUS_API_KEY
        }
        
        response_data = await self._request(
            method="GET",
            endpoint="properties",
            headers=headers
        )
        return response_data
    
    async def get_property_by_id(self, property_id: int, inmobiliaria_id: int = 1) -> dict:
        headers = {
            "Authorization": DOMUS_API_KEY,
            "inmobiliaria": str(inmobiliaria_id)
        }
        response_data = await self._request(
            method="GET",
            endpoint=f"properties/{property_id}",
            headers=headers
        )
        return response_data