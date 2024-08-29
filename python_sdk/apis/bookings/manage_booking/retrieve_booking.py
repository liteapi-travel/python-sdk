# python_sdk/apis/bookings/manage_booking/retrieve_booking.py

from typing import Dict, Any, Optional
from python_sdk.client import LiteApiClient

class RetrieveBookingApi:
    def __init__(self, client: LiteApiClient):
        self.client = client

    def retrieve_booking(
        self,
        booking_id: str,
        timeout: Optional[float] = 4.0
    ) -> Dict[str, Any]:
        """
        Retrieve a booking by its unique booking ID.

        :param booking_id: The unique identifier of the booking to retrieve.
        :param timeout: Request timeout in seconds.
        :return: JSON response containing the booking details.
        """

        endpoint = f"{self.client.base_url}/bookings/{booking_id}"
        params = {
            "timeout": timeout,
        }

        headers = {
            "accept": "application/json",
            "X-API-Key": self.client.api_key
        }

        response = self.client.get(endpoint, params=params, headers=headers)

        return response.json()
