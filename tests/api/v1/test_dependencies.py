from typing import Any, Optional

import pytest

from misp_gateway.api.v1.dependencies import is_truthy


@pytest.mark.parametrize("v,expected", [(None, True), ("True", True), ("False", False)])
def test_is_truthy(v: Optional[Any], expected: bool):
    assert is_truthy(v) is expected
