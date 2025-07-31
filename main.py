from fastapi import FastAPI
from app.api.api_router import api_router
from app.core.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api_router, prefix="/api")
