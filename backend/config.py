"""Config file."""
from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Bike Stats"
    cors_allow_origin: str = "http://localhost.com,http://localhost:8080," \
                             "http://localhost:8000,http://127.0.0.1:8000,*"
    cors_allow_credentials: bool = True
    cors_allow_methods: str = "GET,HEAD,POST,OPTIONS,PUT,PATCH,DELETE"
    cors_allow_headers: str = "Access-Token,Content-Type,referrer," \
                              "Authorization,Cache-Control,X-Requested-With"
    log_path: str = '/tmp/app.log'
    error_log_path: str = '/tmp/app-error.log'

    app_token: str = 's0m3customT0k3n'

    sqlalchemy_database_url = "sqlite:///./sql_app.db"

    # MAX_NAME_LENGTH
    max_context_name_length = 12

    # Max number of context
    max_context_per_user = 10

    class Config:
        env_file = ".env"       # Change this to the desired dotenv file


@lru_cache()
def get_config():
    return Settings()
