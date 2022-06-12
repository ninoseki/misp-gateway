from typing import Any

from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse

from misp_gateway.api.v1.dependencies import get_forwarder
from misp_gateway.forwarder import Forwarder
from misp_gateway.transformers import get_misp_event_transform_functions

router = APIRouter()


def apply_transform_functions(
    payload: dict[Any, Any], *, request: Request
) -> dict[Any, Any]:
    funcs = get_misp_event_transform_functions()
    for func in funcs:
        payload = func(payload, request)

    return payload


@router.post("/add")
def add_event(
    payload: dict, *, forwarder: Forwarder = Depends(get_forwarder), request: Request
):
    payload = apply_transform_functions(payload, request=request)
    res = forwarder.post("/events/add", payload)
    return JSONResponse(content=res.json(), status_code=res.status_code)


@router.put("/edit/{event_id}")
def edit_event_by_put(
    event_id: str,
    payload: dict,
    *,
    forwarder: Forwarder = Depends(get_forwarder),
    request: Request,
):
    payload = apply_transform_functions(payload, request=request)
    res = forwarder.put(f"/events/edit/{event_id}", payload)
    return JSONResponse(content=res.json(), status_code=res.status_code)


@router.post("/edit/{event_id}")
def edit_event_by_post(
    event_id: str,
    payload: dict,
    *,
    forwarder: Forwarder = Depends(get_forwarder),
    request: Request,
):
    payload = apply_transform_functions(payload, request=request)
    res = forwarder.post(f"/events/edit/{event_id}", payload)
    return JSONResponse(content=res.json(), status_code=res.status_code)
