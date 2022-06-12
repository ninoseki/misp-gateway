import pytest
from fastapi.testclient import TestClient

from misp_gateway.main import create_app


@pytest.fixture
async def client():
    app = create_app()
    yield TestClient(app)
