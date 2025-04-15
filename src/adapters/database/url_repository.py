from typing import Optional
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.entities.url import URL
from src.core.ports.url_repository import URLRepository
from src.adapters.database.models import URL as URLModel

class SQLAlchemyURLRepository(URLRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, url: URL) -> None:
        url_model = URLModel(
            id=url.id,
            original_url=url.original_url,
            short_code=url.short_code,
            created_at=url.created_at,
            updated_at=url.updated_at,
            access_count=url.access_count
        )
        self.session.add(url_model)
        await self.session.commit()

    async def get_by_short_code(self, short_code: str) -> Optional[URL]:
        result = await self.session.execute(
            select(URLModel).where(URLModel.short_code == short_code)
        )
        url_model = result.scalar_one_or_none()
        if url_model:
            return URL(
                id=url_model.id,
                original_url=url_model.original_url,
                short_code=url_model.short_code,
                created_at=url_model.created_at,
                updated_at=url_model.updated_at,
                access_count=url_model.access_count
            )
        return None

    async def get_by_id(self, id: UUID) -> Optional[URL]:
        result = await self.session.execute(
            select(URLModel).where(URLModel.id == id)
        )
        url_model = result.scalar_one_or_none()
        if url_model:
            return URL(
                id=url_model.id,
                original_url=url_model.original_url,
                short_code=url_model.short_code,
                created_at=url_model.created_at,
                updated_at=url_model.updated_at,
                access_count=url_model.access_count
            )
        return None

    async def delete(self, id: UUID) -> None:
        result = await self.session.execute(
            select(URLModel).where(URLModel.id == id)
        )
        url_model = result.scalar_one_or_none()
        if url_model:
            await self.session.delete(url_model)
            await self.session.commit()

    async def exists_by_short_code(self, short_code: str) -> bool:
        result = await self.session.execute(
            select(URLModel).where(URLModel.short_code == short_code)
        )
        return result.scalar_one_or_none() is not None 