from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '.env')
load_dotenv(env_path)


class Settings(BaseSettings):
    database_url: str
    port: int = 8000
    echo_sql: bool = True
    test: bool = False
    project_name: str = "My FastAPI project"
    oauth_token_secret: str = "my_dev_secret"
    log_level: str = "DEBUG"


settings = Settings()  # type: ignore
