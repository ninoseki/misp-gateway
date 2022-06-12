from typing import Any, Optional

import httpx


class Forwarder:
    def __init__(self, misp_url: str, misp_api_key: str, *, verify_ssl: bool):
        self.misp_url = misp_url
        self.misp_api_key = misp_api_key
        self.verify_ssl = verify_ssl

        self.headers = {
            "authorization": self.misp_api_key,
            "accept": "application/json",
        }

    def url_for(self, path: str) -> str:
        return self.misp_url + path

    def post(self, path: str, payload: dict[Any, Any]) -> httpx.Response:
        url = self.url_for(path)
        return httpx.post(
            url, json=payload, headers=self.headers, verify=self.verify_ssl
        )

    def put(self, path: str, payload: dict[Any, Any]) -> httpx.Response:
        url = self.url_for(path)
        return httpx.put(
            url, json=payload, headers=self.headers, verify=self.verify_ssl
        )

    def get(self, path: str, params: Optional[dict[Any, Any]] = None) -> httpx.Response:
        url = self.url_for(path)
        return httpx.get(
            url, params=params, headers=self.headers, verify=self.verify_ssl
        )

    def delete(
        self, path: str, params: Optional[dict[Any, Any]] = None
    ) -> httpx.Response:
        url = self.url_for(path)
        return httpx.delete(
            url, params=params, headers=self.headers, verify=self.verify_ssl
        )
