from pydantic import BaseModel


class CreateUrlRequest(BaseModel):
    url: str


class UrlResponse(BaseModel):
    id: int
    url: str
    short_code: str
    created_at: str
    updated_at: str


class UrlStatisticsResponse(UrlResponse):
    access_count: int
