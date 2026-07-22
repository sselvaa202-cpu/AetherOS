from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str
    app_version: str
    debug: bool

    secret_key: str
    database_url: str

    access_token_expire_minutes: int
    algorithm: str

    # OpenRouter
    openrouter_api_key: str
    openrouter_base_url: str

    # LLM
    llm_provider: str
    llm_model: str
    llm_max_tokens: int
    llm_temperature: float

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


settings = Settings()