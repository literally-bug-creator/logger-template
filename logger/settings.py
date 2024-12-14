from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class LoggerSettings(BaseSettings):
    LEVEL: int = Field(default=0)
    FILENAME: str = Field(default="app.log")
    BACKUP_COUNT: int = Field(default=4)
    MAX_BYTES: int = Field(default=102400)
    ROTATING_INTERVAL: int = Field(default=1)
    ROTATING_PER: str = Field(default="d")
    
    model_config = SettingsConfigDict(
        env_file="env.logger"
    )