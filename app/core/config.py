from datetime import timedelta
import os
from dotenv import load_dotenv

load_dotenv()

DOMUS_API_KEY = os.getenv("DOMUS_API_KEY")
DOMUS_URL = os.getenv("DOMUS_URL", "https://newapi.domus.la")

ENV = os.getenv("ENV")

SECRET_KEY = os.getenv("SECRET_KEY", "SECRET_KEY_CHANGE_ME")
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 15))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", 30))