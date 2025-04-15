from typing import Optional
from uuid import UUID

from src.core.entities.url import URL

class URLRepository:
    async def save(self, url: URL) -> None:
        raise NotImplementedError

    async def get_by_short_code(self, short_code: str) -> Optional[URL]:
        raise NotImplementedError

    async def get_by_id(self, id: UUID) -> Optional[URL]:
        raise NotImplementedError

    async def delete(self, id: UUID) -> None:
        raise NotImplementedError

    async def exists_by_short_code(self, short_code: str) -> bool:
        raise NotImplementedError 