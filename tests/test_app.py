from fastapi.testclient import TestClient


def test_index(client: TestClient):
    res = client.get("/", allow_redirects=False)
    assert res.status_code == 307
    assert res.headers.get("location") == "/redoc"
