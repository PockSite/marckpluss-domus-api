from app.client.client import BaseExternalClient
from app.core.config import DOMUS_API_KEY, DOMUS_URL

class DomusClient(BaseExternalClient[dict]):
    def __init__(self, timeout=10):
        super().__init__(DOMUS_URL, timeout)

    async def get_all_properties(self, inmobiliaria_id: int = 1, per_page: int = 50) -> dict:
        headers = {
            "inmobiliaria": str(inmobiliaria_id),
            "perpage": str(per_page),
            "Authorization": DOMUS_API_KEY
        }

        page = 1
        all_data = []

        # Primera petición (para obtener metadata)
        first_response = await self._request(
            method="GET",
            endpoint=f"properties?page=1",
            headers=headers
        )

        total = first_response.get("total", 0)
        last_page = first_response.get("last_page", 1)

        all_data.extend(first_response.get("data", []))

        # Traer el resto de páginas
        for page in range(2, last_page + 1):
            response = await self._request(
                method="GET",
                endpoint=f"properties?page={page}",
                headers=headers
            )
            all_data.extend(response.get("data", []))

        # Construir respuesta final respetando formato
        return {
            "total": total,
            "per_page": per_page,
            "current_page": 1,
            "last_page": last_page,
            "from": 1,
            "to": len(all_data),
            "data": all_data
        }