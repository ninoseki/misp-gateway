from typing import Any, Optional

from fastapi import Request

from misp_gateway.core import settings
from misp_gateway.forwarder import Forwarder


def is_truthy(v: Optional[Any], *, default: bool = True) -> bool:
    if v is None:
        return default

    if isinstance(v, bool):
        return v

    return str(v).upper() == "TRUE"


def get_forwarder(request: Request) -> Forwarder:
    misp_url = str(request.headers.get("x-misp-url", settings.MISP_URL))
    misp_api_key = str(request.headers.get("authorization", settings.MISP_API_KEY))
    verify_ssl = request.headers.get("x-misp-verify-ssl", settings.MISP_VERIFY_SSL)
    return Forwarder(misp_url, misp_api_key, verify_ssl=is_truthy(verify_ssl))
