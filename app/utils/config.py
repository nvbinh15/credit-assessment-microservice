from pydantic import BaseSettings 
import os 

class Settings(BaseSettings):

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    SECRET_KEY: str = os.getenv('SECRET_KEY')

    class Config:
        env_file = '../.env'


settings = Settings()