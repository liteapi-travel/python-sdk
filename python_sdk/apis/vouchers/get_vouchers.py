# python_sdk/apis/vouchers/get_vouchers.py

from typing import Dict, Any
from python_sdk.client import LiteApiClient

class GetVouchersApi:
    def __init__(self, client: LiteApiClient):
        self.client = client

    def retrieve_all_vouchers(self) -> Dict[str, Any]:
        endpoint = f"{self.client.service_url}/vouchers"
        response = self.client.get(endpoint)
        return response
