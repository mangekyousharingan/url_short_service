from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

class URL:
    def __init__(
        self,
        id: UUID,
        original_url: str,
        short_code: str,
        created_at: datetime,
        updated_at: datetime,
        access_count: int = 0
    ):
        self.id = id
        self.original_url = original_url
        self.short_code = short_code
        self.created_at = created_at
        self.updated_at = updated_at
        self.access_count = access_count

    @classmethod
    def create(cls, original_url: str, short_code: str) -> "URL":
        now = datetime.utcnow()
        return cls(
            id=uuid4(),
            original_url=original_url,
            short_code=short_code,
            created_at=now,
            updated_at=now,
            access_count=0
        )

    def increment_access_count(self) -> None:
        self.access_count += 1
        self.updated_at = datetime.utcnow()

    def update_url(self, new_url: str) -> None:
        self.original_url = new_url
        self.updated_at = datetime.utcnow() 