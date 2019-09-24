from typing import Optional

from httpx import Client


class HTTPClient:
    def __init__(
        self,
        base_url: str,
        host: str,
        default_headers: Optional[dict] = None,
        default_params: Optional[dict] = None,
    ):
        self.base_url = base_url
        self.host = host
        self.default_headers = default_headers or {}
        self.default_params = default_params or {}

        self.http_client = Client(base_url=self.base_url, headers=default_headers)

    def get(self, url: str, params: dict, headers: dict = None):
        custom_headers = headers or {}

        response = self.http_client.get(
            url=url, params={**params, **self.default_params}, headers=custom_headers
        )

        return response
