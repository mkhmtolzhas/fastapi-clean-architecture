from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Database
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_name: str = "database"

    # Redis
    redis_host: str
    redis_port: int

    # JWT
    jwt_secret: str

    class Config:
        env_file = ".env"


    def db_async_url(self):
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
    
    def db_sync_url(self):
        return f"postgresql+psycopg2://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
    
    
    def redis_url(self):
        return f"redis://{self.redis_host}:{self.redis_port}/0"
    


settings = Settings()



