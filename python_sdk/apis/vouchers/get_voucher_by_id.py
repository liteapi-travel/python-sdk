# python_sdk/apis/vouchers/get_voucher_by_id.py

from typing import Dict, Any
from python_sdk.client import LiteApiClient

class GetVoucherByIdApi:
    def __init__(self, client: LiteApiClient):
        self.client = client

    def retrieve_voucher_by_id(self, voucher_id: int) -> Dict[str, Any]:
        endpoint = f"{self.client.service_url}/vouchers/{voucher_id}"
        response = self.client.get(endpoint)
        return response

