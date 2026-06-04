"""
Application configuration loaded from environment variables via Pydantic Settings.
"""
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Application
    APP_NAME: str = "BI Agent Platform"
    APP_ENV: str = "production"
    APP_SECRET_KEY: str = "YOUR_VALUE_HERE"
    DEBUG: bool = False

    # Database
    DATABASE_URL: str = "YOUR_VALUE_HERE"
    POSTGRES_HOST: str = "postgres"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = "bi_agent_db"
    POSTGRES_USER: str = "YOUR_VALUE_HERE"
    POSTGRES_PASSWORD: str = "YOUR_VALUE_HERE"

    # Redis
    REDIS_URL: str = "redis://redis:6379/0"

    # JWT
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    JWT_REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # License
    LICENSE_PUBLIC_KEY: str = "YOUR_VALUE_HERE"

    # Email
    SMTP_HOST: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USERNAME: str = "YOUR_VALUE_HERE"
    SMTP_PASSWORD: str = "YOUR_VALUE_HERE"
    SMTP_FROM_EMAIL: str = "YOUR_VALUE_HERE"
    SMTP_FROM_NAME: str = "BI Agent Platform"

    # Encryption
    ENCRYPTION_KEY: str = "YOUR_VALUE_HERE"

    # Sentry
    SENTRY_DSN: str = ""

    # Optional Modules
    N8N_ENABLED: bool = False

    # File Upload
    MAX_FILE_SIZE_MB: int = 50
    UPLOAD_DIR: str = "/app/uploads"

    # CORS
    ALLOWED_ORIGINS: str = "http://localhost:3000"

    # API Token
    API_TOKEN_EXPIRE_DAYS: int = 90

    # Telegram (optional)
    TELEGRAM_BOT_TOKEN: str = ""
    TELEGRAM_ALERT_CHAT_ID: str = ""

    # Frontend URL
    FRONTEND_URL: str = "http://localhost:3000"

    @property
    def allowed_origins_list(self) -> List[str]:
        return [o.strip() for o in self.ALLOWED_ORIGINS.split(",")]

    @property
    def encryption_key_bytes(self) -> bytes:
        """
        Decode the base64-encoded encryption key.

        Note:
            Key derivation logic is proprietary and not included in this public version.
        """
        raise NotImplementedError("Proprietary implementation")

    @property
    def max_file_size_bytes(self) -> int:
        return self.MAX_FILE_SIZE_MB * 1024 * 1024


settings = Settings()
