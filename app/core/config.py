import secrets

from typing import Optional
from pydantic import BaseSettings
from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    API_URL_PREFIX: Optional[str]
    SECRET_KEY: Optional[str] = secrets.token_urlsafe(32)

    RESET_PASSWORD_TOKEN_EXPIRATION_MINUTES: Optional[int] = 20
    ACCESS_TOKEN_EXPIRE_MINUTES: Optional[int] = 86400
    REGISTER_TOKEN_EXPIRE_MINUTES: Optional[int] = 20

    PROJECT_NAME: Optional[str]
    SQLALCHEMY_DATABASE_URI: Optional[str]
    SMTP_TLS: Optional[bool]
    SMTP_PORT: Optional[int]
    SMTP_HOST: Optional[str]
    SMTP_USER: Optional[str]
    SMTP_PASSWORD: Optional[str]
    BASE_URL: Optional[str]
    APP_URL: Optional[str]

    EMAILS_FROM_EMAIL: Optional[str]
    EMAILS_FROM_NAME: Optional[str]
    EMAIL_RESET_TOKEN_EXPIRE_HOURS: Optional[int] = 48
    
    DEBUG: Optional[bool] = False

    FIRST_SUPERUSER: Optional[str]
    FIRST_SUPERUSER_PASSWORD: Optional[str]

    DKIM_PATH: Optional[str]

    EMAIL_TEMPLATES_DIR: Optional[str]
    SERVER_HOST: Optional[str]
    BACKEND_CORS_ORIGINS: Optional[str]
    REDEFINIR_SENHA_ENDPOINT: Optional[str]
    STATIC_FOLDER: Optional[str]
    UPLOAD_FOLDER: Optional[str]

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
