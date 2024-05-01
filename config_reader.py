from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

load_dotenv()


class Settings(BaseSettings):
    bot_token: SecretStr
    database_name: SecretStr
    mongo_host: SecretStr
    mongo_port: SecretStr
    collection_name: SecretStr

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


config = Settings()
