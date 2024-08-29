# python_sdk/apis/iata_codes/get_iata_codes.py

from typing import Dict, Any, Optional
from python_sdk.client import LiteApiClient

class GetIataCodesApi:
    def __init__(self, client: LiteApiClient):
        self.client = client

    def get_iata_codes(
        self,
        timeout: Optional[float] = 4.0
    ) -> Dict[str, Any]:
        endpoint = f"{self.client.base_url}/data/iataCodes"
        params = {
            "timeout": timeout
        }

        return self.client.get(endpoint, params=params)
