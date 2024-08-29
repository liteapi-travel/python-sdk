# python_sdk/apis/bookings/make_booking/book.py

from typing import Dict, Any, List, Optional
from python_sdk.client import LiteApiClient

class BookApi:
    def __init__(self, client: LiteApiClient):
        self.client = client

    def complete_booking(
        self,
        prebook_id: str,
        client_reference: str,
        holder: Dict[str, str],
        guests: List[Dict[str, str]],
        payment_method: str,
        transaction_id: Optional[str] = None,
        voucher_code: Optional[str] = None
    ) -> Dict[str, Any]:
        
        endpoint = f"{self.client.base_url}/rates/book"
        payload = {
            "prebookId": prebook_id,
            "clientReference": client_reference,
            "holder": holder,
            "guests": guests,
            "payment": {
                "method": payment_method,
            }
        }

        if transaction_id:
            payload["payment"]["transactionId"] = transaction_id

        if voucher_code:
            payload["voucherCode"] = voucher_code

        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "X-API-Key": self.client.api_key
        }

        response = self.client.post(endpoint, json=payload, headers=headers)

        return response.json()
