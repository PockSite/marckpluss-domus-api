from fastapi import FastAPI
from app.api.v1.router import router
from app.core.config import CORS
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
def health():
    return {"status": "ok"}

@app.head("/")
def health_head():
    return {"status": "ok"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS,           
    allow_credentials=True,       
    allow_methods=["*"],            
    allow_headers=["*"],         
)

app.include_router(router, prefix="/api/v1")

