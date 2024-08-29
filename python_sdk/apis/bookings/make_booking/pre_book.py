# python_sdk/apis/bookings/make_booking/pre_book.py

from typing import Dict, Any, Optional
from python_sdk.client import LiteApiClient

class PreBookApi:
    def __init__(self, client: LiteApiClient):
        self.client = client

    def create_checkout_session(
        self,
        offer_id: str,
        use_payment_sdk: bool,
        voucher_code: Optional[str] = None
    ) -> Dict[str, Any]:
       
        endpoint = f"{self.client.book_service_url}/rates/prebook"
        payload = {
            "offerId": offer_id,
            "usePaymentSdk": use_payment_sdk
        }

        if voucher_code:
            payload["voucherCode"] = voucher_code

        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "X-API-Key": self.client.api_key
        }

        response = self.client.post(endpoint, data=payload, headers=headers)

        return response
