from typing import List

from pydantic_settings import BaseSettings
from sqlalchemy.ext.asyncio import create_async_engine


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/url_shortener"
    CORS_ORIGINS: List[str] = ["*"]
    ENVIRONMENT: str = "development"

    @property
    def engine(self):
        return create_async_engine(self.DATABASE_URL)

    # Database
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str
    postgres_port: int

    # Application
    app_host: str
    app_port: int

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
