from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/flightdb"
    CAMEL_ROUTE_PATH: str = "camel/routes.xml"
    API_PREFIX: str = "/api/v1"

    class Config:
        env_file = ".env"

settings = Settings()