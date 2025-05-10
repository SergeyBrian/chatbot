from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    db_name: str = "db"
    db_user: str = "postgres"
    db_password: str = "postgres"
    db_host: str = "localhost"
    db_port: int = 5432

    model_config = SettingsConfigDict(fields={
        "db_name": {"env": "DB_NAME"},
        "db_user": {"env": "DB_USER"},
        "db_password": {"env": "DB_PASSWORD"},
        "db_host": {"env": "DB_HOST"},
        "db_port": {"env": "DB_PORT"},
    })

    @property
    def dsn(self) -> str:
        return f"dbname={self.db_name} user={self.db_user} password={self.db_password} host={self.db_host} port={self.db_port} sslmode=disable"


settings = Settings()
