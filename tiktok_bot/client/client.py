from time import time
from typing import Optional

from httpx import Client

from .utils import generate_as, generate_cp, generate_mas


class HTTPClient:
    def __init__(
        self,
        base_url: str,
        default_headers: Optional[dict] = None,
        default_params: Optional[dict] = None,
    ):
        self.base_url = base_url
        self.default_headers = default_headers or {}
        self.default_params = default_params or {}

        self.http_client = Client(
            base_url=self.base_url, headers=default_headers, params=self.default_params
        )

    def get(self, url: str, params: dict, headers: Optional[dict] = None):
        custom_headers = headers or {}

        response = self.http_client.get(
            url=url, params={**self._generate_params(), **params}, headers=custom_headers
        )

        return response

    def post(
        self, url: str, data: dict, headers: Optional[dict] = None, params: Optional[dict] = None
    ):
        custom_headers = headers or {}
        custom_params = params or {}

        response = self.http_client.post(
            url=url,
            params={**self._generate_params(), **custom_params},
            data=data,
            headers=custom_headers,
        )

        return response

    def _generate_params(self):
        now = str(int(round(time() * 1000)))

        params = {
            "_rticket": now,
            "ts": now,
            "mas": generate_mas(now),
            "as": generate_as(now),
            "cp": generate_cp(now),
        }

        return params
