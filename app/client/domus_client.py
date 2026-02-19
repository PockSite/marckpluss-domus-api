from app.client.client import BaseExternalClient
from app.core.config import DOMUS_API_KEY, DOMUS_URL


class DomusClient(BaseExternalClient):
    def __init__(self):
        super().__init__(
            base_url=DOMUS_URL, 
            api_key=DOMUS_API_KEY
        )

    async def obtener_inmueble(self, inmueble_id: str):
        # Usamos el método 'get' del padre
        return await self.get(f"properties/{inmueble_id}")

    async def listar_inmuebles(self, filtros: dict):
        return await self.get("properties", params=filtros)