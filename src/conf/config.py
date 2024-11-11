import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    DEBUG: bool = os.getenv("SUPERBENCHMARK_DEBUG", "False").lower() in ("true", "1")


settings = Settings()
