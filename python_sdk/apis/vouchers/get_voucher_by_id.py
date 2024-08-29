# python_sdk/apis/vouchers/get_voucher_by_id.py

from typing import Dict, Any
from python_sdk.client import LiteApiClient

class GetVoucherByIdApi:
    def __init__(self, client: LiteApiClient):
        self.client = client

    def retrieve_voucher_by_id(self, voucher_id: int) -> Dict[str, Any]:
        """
        Fetch detailed information about a specific voucher using its unique identifier.
        This includes the voucher code, discount details, usage limits, and more.

        :param voucher_id: The unique identifier of the voucher to retrieve.
        :return: JSON response containing the voucher details.
        """
        endpoint = f"{self.client.base_url}/vouchers/{voucher_id}"
        headers = {
            "accept": "application/json",
            "X-API-Key": self.client.api_key
        }

        response = self.client.get(endpoint, headers=headers)

        return response.json()
