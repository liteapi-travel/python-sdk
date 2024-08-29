# python_sdk/apis/city/get_cities_by_country_code.py

from typing import Dict, Any, Optional
from python_sdk.client import LiteApiClient

class GetCitiesByCountryCodeApi:
    def __init__(self, client: LiteApiClient):
        self.client = client

    def get_cities(
        self,
        country_code: str,
        timeout: Optional[float] = 4.0
    ) -> Dict[str, Any]:
        endpoint = f"{self.client.base_url}/data/cities"
        params = {
            "countryCode": country_code,
            "timeout": timeout
        }

        return self.client.get(endpoint, params=params)
