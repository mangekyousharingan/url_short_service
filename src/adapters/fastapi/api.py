from fastapi import APIRouter

from src.adapters.fastapi.schemas import (
    CreateUrlRequest,
    UrlResponse,
    UrlStatisticsResponse,
)

api_router = APIRouter(prefix="/v1")


@api_router.get("/shorten/{short_code}", response_model=UrlResponse)
def retrieve_original_url(short_code: str) -> UrlResponse:
    pass


@api_router.post("/shorten", response_model=UrlResponse)
def create_short_url(request: CreateUrlRequest) -> UrlResponse:
    pass


@api_router.put("/shorten/{short_code}", response_model=UrlResponse)
def update_short_url(short_code: str) -> UrlResponse:
    pass


@api_router.delete("/shorten/{short_code}", response_model=UrlStatisticsResponse)
def delete_short_url(short_code: str) -> UrlStatisticsResponse:
    pass
