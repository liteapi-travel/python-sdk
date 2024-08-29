# python_sdk/apis/loyalty/get_loyalty.py

from typing import Dict, Any
from python_sdk.client import LiteApiClient

class GetLoyaltyApi:
    def __init__(self, client: LiteApiClient):
        self.client = client

    def get_loyalty_program_settings(self) -> Dict[str, Any]:
        """
        Retrieves information about current loyalty program settings, including status and cashback rates.

        :return: JSON response containing the loyalty program settings.
        """

        endpoint = f"{self.client.base_url}/loyalties"
        headers = {
            "accept": "application/json",
            "X-API-Key": self.client.api_key
        }

        response = self.client.get(endpoint, headers=headers)

        return response.json()
