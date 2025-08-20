from pathlib import Path
import os
from dotenv import load_dotenv

def load_env(dotenv_path: str | None = None) -> None:
    if dotenv_path is None:
        dotenv_path = Path(__file__).resolve().parents[1] / ".env"
    load_dotenv(dotenv_path, override=False)

def get_key(key: str, default=None):
    return os.getenv(key, default)
