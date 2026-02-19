
from fastapi import Depends
from app.client.domus_client import DomusClient
from app.service.domus_service import DomusService

def get_domus_service(client: DomusClient = Depends()):
    return DomusService(client)
