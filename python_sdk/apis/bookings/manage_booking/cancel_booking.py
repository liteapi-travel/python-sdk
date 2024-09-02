# python_sdk/apis/bookings/manage_booking/cancel_booking.py

from typing import Dict, Any, Optional
from python_sdk.client import LiteApiClient

class CancelBookingApi:
    def __init__(self, client: LiteApiClient):
        self.client = client

    def cancel_booking(
        self,
        booking_id: str,
        timeout: Optional[float] = 4.0
    ) -> Dict[str, Any]:
        endpoint = f"/bookings/{booking_id}"
        
        headers = {
            "accept": "application/json",
            "X-API-Key": self.client.api_key
        }

        response = self.client.put(endpoint, data={"timeout": timeout}, headers=headers, use_service="booking")

        return response

