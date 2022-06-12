from typing import Any

from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse

from misp_gateway.api.v1.dependencies import get_forwarder
from misp_gateway.forwarder import Forwarder
from misp_gateway.transformers import get_misp_attribute_transform_functions

router = APIRouter()


def apply_transform_functions(
    payload: dict[Any, Any], *, request: Request
) -> dict[Any, Any]:
    funcs = get_misp_attribute_transform_functions()
    for func in funcs:
        payload = func(payload, request)

    return payload


@router.post("/add/{event_id}")
def add_attribute(
    event_id: str,
    payload: dict[Any, Any],
    *,
    forwarder: Forwarder = Depends(get_forwarder),
    request: Request,
):
    payload = apply_transform_functions(payload, request=request)
    res = forwarder.post(f"/attributes/add/{event_id}", payload)
    return JSONResponse(content=res.json(), status_code=res.status_code)


@router.put("/edit/{attribute_id}")
def edit_attribute_by_put(
    attribute_id: str,
    payload: dict,
    *,
    forwarder: Forwarder = Depends(get_forwarder),
    request: Request,
):
    payload = apply_transform_functions(payload, request=request)
    res = forwarder.put(f"/attributes/add/{attribute_id}", payload)
    return JSONResponse(content=res.json(), status_code=res.status_code)


@router.post("/edit/{attribute_id}")
def edit_attribute_by_post(
    attribute_id: str,
    payload: dict,
    *,
    forwarder: Forwarder = Depends(get_forwarder),
    request: Request,
):
    payload = apply_transform_functions(payload, request=request)
    res = forwarder.post(f"/attributes/add/{attribute_id}", payload)
    return JSONResponse(content=res.json(), status_code=res.status_code)
