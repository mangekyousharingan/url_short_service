from typing import Optional
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, HttpUrl

from src.core.entities.url import URL
from src.core.services.url_service import URLService
from src.adapters.database.session import get_db_session
from src.adapters.database.url_repository import SQLAlchemyURLRepository

router = APIRouter(prefix="/shorten", tags=["urls"])

class CreateURLRequest(BaseModel):
    url: HttpUrl

class URLResponse(BaseModel):
    id: UUID
    url: str
    short_code: str
    created_at: str
    updated_at: str
    access_count: Optional[int] = None

    @classmethod
    def from_entity(cls, url: URL) -> "URLResponse":
        return cls(
            id=url.id,
            url=url.original_url,
            short_code=url.short_code,
            created_at=url.created_at.isoformat(),
            updated_at=url.updated_at.isoformat(),
            access_count=url.access_count
        )

@router.post("", response_model=URLResponse, status_code=status.HTTP_201_CREATED)
async def create_short_url(
    request: CreateURLRequest,
    session=Depends(get_db_session)
) -> URLResponse:
    url_service = URLService(SQLAlchemyURLRepository(session))
    url = await url_service.create_short_url(str(request.url))
    return URLResponse.from_entity(url)

@router.get("/{short_code}", response_model=URLResponse)
async def get_url(
    short_code: str,
    session=Depends(get_db_session)
) -> URLResponse:
    url_service = URLService(SQLAlchemyURLRepository(session))
    url = await url_service.get_url_by_short_code(short_code)
    if not url:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="URL not found"
        )
    return URLResponse.from_entity(url)

@router.put("/{short_code}", response_model=URLResponse)
async def update_url(
    short_code: str,
    request: CreateURLRequest,
    session=Depends(get_db_session)
) -> URLResponse:
    url_service = URLService(SQLAlchemyURLRepository(session))
    url = await url_service.get_url_by_short_code(short_code)
    if not url:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="URL not found"
        )
    updated_url = await url_service.update_url(url.id, str(request.url))
    return URLResponse.from_entity(updated_url)

@router.delete("/{short_code}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_url(
    short_code: str,
    session=Depends(get_db_session)
) -> None:
    url_service = URLService(SQLAlchemyURLRepository(session))
    url = await url_service.get_url_by_short_code(short_code)
    if not url:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="URL not found"
        )
    await url_service.delete_url(url.id)

@router.get("/{short_code}/stats", response_model=URLResponse)
async def get_url_stats(
    short_code: str,
    session=Depends(get_db_session)
) -> URLResponse:
    url_service = URLService(SQLAlchemyURLRepository(session))
    url = await url_service.get_url_by_short_code(short_code)
    if not url:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="URL not found"
        )
    return URLResponse.from_entity(url) 