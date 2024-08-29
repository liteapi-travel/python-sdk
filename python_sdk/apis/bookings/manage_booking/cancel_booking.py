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
         
        endpoint = f"{self.client.book_service_url}/bookings/{booking_id}"

        params = {
            "timeout": timeout,
        }

        response = self.client.post(endpoint, data=params)

        return response
