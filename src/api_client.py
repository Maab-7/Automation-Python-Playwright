from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import requests


@dataclass
class ApiClient:
    base_url: str
    headers: dict[str, str]
    session: requests.Session

    def _url(self, path: str) -> str:
        return f"{self.base_url.rstrip('/')}/{path.lstrip('/')}"

    def get(self, path: str, **kwargs: Any) -> requests.Response:
        return self.session.get(
            self._url(path), headers=self.headers, timeout=10, **kwargs
        )

    def post(
        self, path: str, json: dict[str, Any] | None = None, **kwargs: Any
    ) -> requests.Response:
        return self.session.post(
            self._url(path), headers=self.headers, json=json, timeout=10, **kwargs
        )
