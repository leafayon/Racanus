from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    racanus_api_host: str
    racanus_api_port: int

    racanus_database_name: str
