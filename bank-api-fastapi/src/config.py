from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Bank API"
    secret_key: str = "supersecret"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

settings = Settings()