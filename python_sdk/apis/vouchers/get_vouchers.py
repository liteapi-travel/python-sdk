# python_sdk/apis/vouchers/get_vouchers.py

from typing import Dict, Any
from python_sdk.client import LiteApiClient

class GetVouchersApi:
    def __init__(self, client: LiteApiClient):
        self.client = client

    def retrieve_all_vouchers(self) -> Dict[str, Any]:
        """
        Fetch a list of all available vouchers. This endpoint provides details such as the voucher code,
        discount type and value, validity period, and other relevant information.

        :return: JSON response containing the list of all vouchers.
        """
        endpoint = f"{self.client.base_url}/vouchers"
        headers = {
            "accept": "application/json",
            "X-API-Key": self.client.api_key
        }

        response = self.client.get(endpoint, headers=headers)

        return response.json()
