# python_sdk/apis/country/get_countries.py

from typing import Dict, Any, Optional
from python_sdk.client import LiteApiClient

class GetCountriesApi:
    def __init__(self, client: LiteApiClient):
        self.client = client

    def get_countries(
        self,
        timeout: Optional[float] = 4.0
    ) -> Dict[str, Any]:
        endpoint = f"{self.client.base_url}/data/countries"
        params = {
            "timeout": timeout
        }

        return self.client.get(endpoint, params=params)
