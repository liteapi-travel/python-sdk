# python_sdk/apis/bookings/manage_booking/list_bookings.py

from typing import Dict, Any, Optional
from python_sdk.client import LiteApiClient

class ListBookingsApi:
    def __init__(self, client: LiteApiClient):
        self.client = client

    def list_bookings(
        self,
        client_reference: Optional[str] = None,
        timeout: Optional[float] = 4.0
    ) -> Dict[str, Any]:
       
        endpoint = f"{self.client.base_url}/bookings"
        params = {
            "timeout": timeout,
        }

        if client_reference:
            params["clientReference"] = client_reference

        headers = {
            "accept": "application/json",
            "X-API-Key": self.client.api_key
        }

        response = self.client.get(endpoint, params=params, headers=headers)

        return response.json()
