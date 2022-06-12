from fastapi import APIRouter

from .endpoints import attributes, catcher, events

api_router = APIRouter()

api_router.include_router(attributes.router, prefix="/attributes", tags=["attribute"])
api_router.include_router(events.router, prefix="/events", tags=["event"])
api_router.include_router(catcher.router)
