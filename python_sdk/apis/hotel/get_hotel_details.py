# python_sdk/apis/hotel/get_hotel_details.py

from typing import Dict, Any, Optional
from python_sdk.client import LiteApiClient

class GetHotelDetailsApi:
    def __init__(self, client: LiteApiClient):
        self.client = client

    def get_hotel_details(
        self,
        hotel_id: str,
        timeout: Optional[float] = 4.0
    ) -> Dict[str, Any]:
        endpoint = f"{self.client.base_url}/data/hotel"
        params = {
            "hotelId": hotel_id,
            "timeout": timeout
        }

        return self.client.get(endpoint, params=params)
