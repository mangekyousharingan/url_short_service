import string
import random
from typing import Optional
from uuid import UUID

from src.core.entities.url import URL
from src.core.ports.url_repository import URLRepository

class URLService:
    def __init__(self, url_repository: URLRepository):
        self.url_repository = url_repository

    async def create_short_url(self, original_url: str) -> URL:
        short_code = self._generate_short_code()
        while await self.url_repository.exists_by_short_code(short_code):
            short_code = self._generate_short_code()

        url = URL.create(original_url, short_code)
        await self.url_repository.save(url)
        return url

    async def get_url_by_short_code(self, short_code: str) -> Optional[URL]:
        url = await self.url_repository.get_by_short_code(short_code)
        if url:
            url.increment_access_count()
            await self.url_repository.save(url)
        return url

    async def get_url_by_id(self, id: UUID) -> Optional[URL]:
        return await self.url_repository.get_by_id(id)

    async def update_url(self, id: UUID, new_url: str) -> Optional[URL]:
        url = await self.url_repository.get_by_id(id)
        if url:
            url.update_url(new_url)
            await self.url_repository.save(url)
        return url

    async def delete_url(self, id: UUID) -> None:
        await self.url_repository.delete(id)

    def _generate_short_code(self, length: int = 6) -> str:
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length)) 