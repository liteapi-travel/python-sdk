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
        """
        Request a cancellation of an existing confirmed booking.

        :param booking_id: The unique identifier of the booking to cancel.
        :param timeout: Request timeout in seconds.
        :return: JSON response containing the cancellation status.
        """

        endpoint = f"{self.client.base_url}/bookings/{booking_id}"
        params = {
            "timeout": timeout,
        }

        headers = {
            "accept": "application/json",
            "X-API-Key": self.client.api_key
        }

        response = self.client.put(endpoint, params=params, headers=headers)

        return response.json()
