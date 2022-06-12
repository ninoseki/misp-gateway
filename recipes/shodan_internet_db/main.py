from typing import Any, cast

import httpx
from fastapi import FastAPI, Request

from misp_gateway.main import create_app
from misp_gateway.transformers.event import add_misp_event_transform_function

# Enrich an IP address attribute by Shodan Internet DB when creating an event
# Usage:
# $ uvicorn recipes.shodan_internet_db.main:app


def lookup(ip_addr: str):
    res = httpx.get(f"https://internetdb.shodan.io/{ip_addr}")
    res.raise_for_status()

    data = cast(dict, res.json())
    return cast(list[str], data.get("hostnames", []))


def enrich_ip_address_attributes_by_shodan_internet_db(
    payload: dict[Any, Any], request: Request
) -> dict[Any, Any]:
    if request.url.path != "/events/add":
        return payload

    attributes = cast(list[dict], payload.get("Attribute", []))
    enriched: list[dict] = []
    for attribute in attributes:
        if attribute is None:
            continue

        enriched.append(attribute)

        attribute_type = attribute.get("type", "")
        if attribute_type not in ["ip-dst", "ip-src"]:
            continue

        value = attribute.get("value", "")
        hostnames = lookup(value)
        for hostname in hostnames:
            enriched.append(
                {"type": "domain", "category": "Network activity", "value": hostname}
            )

    payload["Attribute"] = enriched
    return payload


def on_startup(
    app: FastAPI,
):
    async def start_app() -> None:
        add_misp_event_transform_function(
            enrich_ip_address_attributes_by_shodan_internet_db
        )

    return start_app


app = create_app(on_startup=on_startup)
