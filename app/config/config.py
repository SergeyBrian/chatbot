from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_name: str = "db"
    db_user: str = "postgres"
    db_password: str = "postgres"
    db_host: str = "localhost"
    db_port: int = 5432

    @property
    def dsn(self) -> str:
        return f"dbname={self.db_name} user={self.db_user} password={self.db_password} host={self.db_host} port={self.db_port} sslmode=disable"


settings = Settings()
