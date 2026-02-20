from app.client.domus_client import DomusClient

client = DomusClient(10)

async def getprop():
    response = await client.get_all_properties()
    return response


