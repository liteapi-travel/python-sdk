# python_sdk/apis/loyalty/get_loyalty.py

from typing import Dict, Any
from python_sdk.client import LiteApiClient

class GetLoyaltyApi:
    def __init__(self, client: LiteApiClient):
        self.client = client

    def get_loyalty_program_settings(self) -> Dict[str, Any]:
        
        endpoint = f"{self.client.service_url}/loyalties"
        response = self.client.get(endpoint)
        return response

