# python_sdk/apis/currencies/get_currencies.py

from typing import Dict, Any, Optional
from python_sdk.client import LiteApiClient

class GetCurrenciesApi:
    def __init__(self, client: LiteApiClient):
        self.client = client

    def get_currencies(
        self,
        timeout: Optional[float] = 4.0
    ) -> Dict[str, Any]:
        endpoint = f"{self.client.base_url}/data/currencies"
        params = {
            "timeout": timeout
        }

        return self.client.get(endpoint, params=params)
