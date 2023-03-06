import os
from typing import Literal, Optional

from pydantic import BaseSettings, Field, validator


class BaseSettingsDotEnv(BaseSettings):
    class Config:
        use_enum_values = True


class PgrDB(BaseSettingsDotEnv):
    host: str = Field(..., env="PGR_DATABASE_HOST")
    port: str = Field(..., env="PGR_DATABASE_PORT")
    db: str = Field(..., env="PGR_DATABASE_NAME")
    user: str = Field(..., env="PGR_DATABASE_USER")
    password: str = Field(..., env="PGR_DATABASE_PASSWORD")


class Settings(BaseSettingsDotEnv):
    pgr_db: PgrDB = Field(default_factory=PgrDB)

settings = Settings()
