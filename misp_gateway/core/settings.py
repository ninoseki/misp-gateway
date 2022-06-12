import sys
from typing import TextIO

from starlette.config import Config
from starlette.datastructures import Secret

config = Config(".env")

# general settings
PROJECT_NAME: str = config("PROJECT_NAME", default="misp-gateway")

DEBUG: bool = config("DEBUG", cast=bool, default=False)
TESTING: bool = config("TESTING", cast=bool, default=False)

# log settings
LOG_FILE: TextIO = config("LOG_FILE", default=sys.stderr)
LOG_LEVEL: str = config("LOG_LEVEL", cast=str, default="DEBUG")
LOG_BACKTRACE: bool = config("LOG_BACKTRACE", cast=bool, default=True)

# MISP settings
MISP_URL: str = config("MISP_URL", cast=str, default="http://localhost")
MISP_API_KEY: str = config("MISP_API_KEY", cast=Secret, default="")
MISP_VERIFY_SSL: bool = config("MISP_VERIFY_SSL", cast=bool, default=True)
