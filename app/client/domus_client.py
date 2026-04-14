from app.client.client import BaseExternalClient
from app.core.config import DOMUS_API_KEY, DOMUS_URL
import asyncio

class DomusClient(BaseExternalClient[dict]):
    def __init__(self, timeout = 10):
        super().__init__(DOMUS_URL, timeout)

    

    async def get_all_properties(
        self,
        inmobiliaria_id: int = 1,
        per_page: int = 50,
        max_retries: int = 3,
        delay: float = 0.5
    ) -> dict:

        headers = {
            "inmobiliaria": str(inmobiliaria_id),
            "perpage": str(per_page),
            "Authorization": DOMUS_API_KEY
        }

        async def fetch_page(page: int):
            """Hace request con reintentos"""
            for attempt in range(max_retries):
                try:
                    return await self._request(
                        method="GET",
                        endpoint=f"properties?page={page}",
                        headers=headers
                    )
                except Exception as e:
                    if attempt == max_retries - 1:
                        print(f"❌ Error en página {page}: {e}")
                        return None
                    
                    await asyncio.sleep(1 * (attempt + 1))  # backoff simple

        # 🔹 Primera página
        first_response = await fetch_page(1)

        if not first_response:
            raise Exception("No se pudo obtener la primera página de Domus")

        total = first_response.get("total", 0)
        last_page = first_response.get("last_page", 1)

        all_data = first_response.get("data", [])

        # 🔹 Resto de páginas
        for page in range(2, last_page + 1):
            response = await fetch_page(page)

            if response and "data" in response:
                all_data.extend(response["data"])

            # 🔥 evitar bloqueo de Domus
            await asyncio.sleep(delay)

        # 🔹 Respuesta final (mismo formato)
        return {
            "total": total,
            "per_page": per_page,
            "current_page": 1,
            "last_page": last_page,
            "from": 1,
            "to": len(all_data),
            "data": all_data
        }
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