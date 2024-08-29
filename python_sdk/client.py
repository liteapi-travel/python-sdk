import requests
from typing import Any, Dict, Optional

class LiteApiClient:
    def __init__(self, api_key: str, service_url: str = "https://api.liteapi.travel/v3.0",
                 book_service_url: str = "https://book.liteapi.travel/v3.0",
                 dashboard_url: str = "https://da.liteapi.travel", timeout: int = 10):
        self.api_key = api_key
        self.service_url = service_url
        self.book_service_url = book_service_url
        self.dashboard_url = dashboard_url
        self.timeout = timeout

    def _make_request(self, url: str, method: str = 'GET', headers: Optional[Dict[str, str]] = None,
                      params: Optional[Dict] = None, data: Optional[Dict] = None) -> Dict[str, Any]:
        if headers is None:
            headers = {
                'accept': 'application/json',
                'X-API-Key': self.api_key
            }

        try:
            response = requests.request(method, url, headers=headers, params=params, json=data, timeout=self.timeout)
            response.raise_for_status()

        except requests.exceptions.HTTPError as http_err:
            return {"status": "failed", "error": str(http_err), "details": response.json() if response.content else {}}
        except requests.exceptions.RequestException as req_err:
            return {"status": "failed", "error": str(req_err)}

        return {"status": "success", "data": response.json()}

    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        url = f"{self.service_url}{endpoint}"
        return self._make_request(url, method='GET', params=params)

    def post(self, endpoint: str, data: Optional[Dict] = None, headers: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
        url = f"{self.service_url}{endpoint}"
        return self._make_request(url, method='POST', data=data, headers=headers)
