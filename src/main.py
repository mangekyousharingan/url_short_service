from fastapi import FastAPI

from src.adapters.fastapi.api import api_router

print("Hello from url-short-service!")

app = FastAPI()

app.include_router(api_router)
