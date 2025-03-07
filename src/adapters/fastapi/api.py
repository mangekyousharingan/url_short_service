from fastapi import APIRouter

api_router = APIRouter(prefix="/v1")


@api_router.get("/shorten/{short_code}")
def retrieve_original_url(short_code: str):
    pass


@api_router.post("/shorten")
def create_short_url():
    pass


@api_router.put("/shorten/{short_code}")
def update_short_url(short_code: str):
    pass


@api_router.delete("/shorten/{short_code}")
def delete_short_url(short_code: str):
    pass
