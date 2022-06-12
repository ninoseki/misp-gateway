from typing import Any, cast

import httpx
from fastapi import FastAPI, Request

from misp_gateway.main import create_app
from misp_gateway.transformers.event import add_misp_event_transform_function

CISCO_20K_LIST: list[str] = []

# Reject domain attributes which are listed in CISCO top 20k list when creating an event
# Usage:
# $ uvicorn recipes.reject_cisco_top20k.main:app


def set_cisco_20k_list():
    res = httpx.get(
        "https://raw.githubusercontent.com/MISP/misp-warninglists/main/lists/cisco_top20k/list.json"
    )
    res.raise_for_status()

    data = cast(dict, res.json())
    CISCO_20K_LIST.extend(cast(list[str], data.get("list", [])))


def is_included_in_cisco_20k_list(value: str) -> bool:
    for v in CISCO_20K_LIST:
        if value == v or value.endswith(f".{v}"):
            return True

    return False


def reject_domain_attributes_in_cisco_20k_list(
    payload: dict[Any, Any], request: Request
) -> dict[Any, Any]:
    if request.url.path != "/events/add":
        return payload

    attributes = cast(list[dict], payload.get("Attribute", []))
    filtered: list[dict] = []
    for attribute in attributes:
        if attribute is None:
            continue

        value = attribute.get("value", "")
        if not is_included_in_cisco_20k_list(value):
            filtered.append(attribute)

    payload["Attribute"] = filtered
    return payload


def on_startup(
    app: FastAPI,
):
    async def start_app() -> None:
        set_cisco_20k_list()
        add_misp_event_transform_function(reject_domain_attributes_in_cisco_20k_list)

    return start_app


app = create_app(on_startup=on_startup)
