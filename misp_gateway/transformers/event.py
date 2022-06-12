from typing import Any, Callable

from fastapi import Request

MISP_EVENT_TRANSFORM_FUNCTIONS: list[
    Callable[[dict[Any, Any], Request], dict[Any, Any]]
] = []


def add_misp_event_transform_function(
    func: Callable[[dict[Any, Any], Request], dict[Any, Any]]
):
    MISP_EVENT_TRANSFORM_FUNCTIONS.append(func)


def get_misp_event_transform_functions():
    return MISP_EVENT_TRANSFORM_FUNCTIONS
