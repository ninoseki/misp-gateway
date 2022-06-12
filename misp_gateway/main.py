from typing import Any, Callable, Optional

from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware
from loguru import logger

from .api.v1.api import api_router
from .core import settings
from .views import view_router


def create_app(
    on_startup: Optional[Callable[[FastAPI], Any]] = None,
    on_shutdown: Optional[Callable[[FastAPI], Any]] = None,
) -> FastAPI:
    logger.add(
        settings.LOG_FILE, level=settings.LOG_LEVEL, backtrace=settings.LOG_BACKTRACE
    )

    app = FastAPI(
        debug=settings.DEBUG,
        title=settings.PROJECT_NAME,
    )
    # add middleware
    app.add_middleware(GZipMiddleware, minimum_size=1000)

    # add event handlers
    if on_startup is not None:
        app.add_event_handler("startup", on_startup(app))

    if on_shutdown is not None:
        app.add_event_handler("shutdown", on_shutdown(app))

    # add routes
    app.include_router(view_router)
    app.include_router(api_router)

    return app
