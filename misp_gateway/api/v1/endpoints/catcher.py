from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse

from misp_gateway.api.v1.dependencies import get_forwarder
from misp_gateway.forwarder import Forwarder

router = APIRouter()


@router.api_route("/{path:path}", methods=["GET"], include_in_schema=False)
async def catch_get(
    request: Request, path: str, *, forwarder: Forwarder = Depends(get_forwarder)
) -> JSONResponse:
    res = forwarder.get(f"/{path}")
    return JSONResponse(content=res.json(), status_code=res.status_code)


@router.api_route("/{path:path}", methods=["POST"], include_in_schema=False)
async def catch_post(
    request: Request, path: str, *, forwarder: Forwarder = Depends(get_forwarder)
) -> JSONResponse:
    payload = await request.json()
    res = forwarder.post(f"/{path}", payload)
    return JSONResponse(content=res.json(), status_code=res.status_code)


@router.api_route("/{path:path}", methods=["PUT"], include_in_schema=False)
async def catch_put(
    request: Request, path: str, *, forwarder: Forwarder = Depends(get_forwarder)
) -> JSONResponse:
    payload = await request.json()
    res = forwarder.put(f"/{path}", payload)
    return JSONResponse(content=res.json(), status_code=res.status_code)


@router.api_route("/{path:path}", methods=["DELETE"], include_in_schema=False)
async def catch_delete(
    request: Request, path: str, *, forwarder: Forwarder = Depends(get_forwarder)
) -> JSONResponse:
    res = forwarder.delete(f"/{path}")
    return JSONResponse(content=res.json(), status_code=res.status_code)
