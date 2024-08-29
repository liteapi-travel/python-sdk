# python_sdk/apis/hotel/get_hotel_reviews.py

from typing import Dict, Any, Optional
from python_sdk.client import LiteApiClient

class GetHotelReviewsApi:
    def __init__(self, client: LiteApiClient):
        self.client = client

    def get_hotel_reviews(
        self,
        hotel_id: str,
        limit: Optional[int] = 200,
        timeout: Optional[float] = 4.0
    ) -> Dict[str, Any]:
        endpoint = f"{self.client.base_url}/data/reviews"
        params = {
            "hotelId": hotel_id,
            "limit": limit,
            "timeout": timeout
        }

        return self.client.get(endpoint, params=params)
