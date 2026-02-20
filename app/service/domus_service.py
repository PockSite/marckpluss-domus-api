from app.client.domus_client import DomusClient
class DomusService:
    def __init__(self, client: DomusClient):
        self.client = client

    async def get_available_properties(self, zone: str = None):
        properties = await self.client.get_all_properties()
        
        return properties

    async def get_property_by_id(self, property_id: str):
        return await self.client.get(f"properties/{property_id}")