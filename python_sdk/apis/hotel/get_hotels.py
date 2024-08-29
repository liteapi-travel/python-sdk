# python_sdk/apis/hotel/get_hotels.py

from typing import Dict, Any, Optional
from python_sdk.client import LiteApiClient

class GetHotelsApi:
    def __init__(self, client: LiteApiClient):
        self.client = client

    def get_hotels(
        self,
        country_code: str,
        city_name: Optional[str] = None,
        hotel_name: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        longitude: Optional[float] = None,
        latitude: Optional[float] = None,
        radius: Optional[int] = None,
        ai_search: Optional[str] = None,
        timeout: Optional[float] = None,
        zip_code: Optional[str] = None,
        min_rating: Optional[float] = None,
        min_reviews_count: Optional[int] = None,
        facility_ids: Optional[str] = None,
        hotel_type_ids: Optional[str] = None,
        chain_ids: Optional[str] = None,
        strict_facilities_filtering: Optional[bool] = None,
        star_rating: Optional[str] = None,
        place_id: Optional[str] = None
    ) -> Dict[str, Any]:
        endpoint = f"{self.client.base_url}/data/hotels"
        params = {
            "countryCode": country_code,
            "cityName": city_name,
            "hotelName": hotel_name,
            "offset": offset,
            "limit": limit,
            "longitude": longitude,
            "latitude": latitude,
            "radius": radius,
            "aiSearch": ai_search,
            "timeout": timeout,
            "zip": zip_code,
            "minRating": min_rating,
            "minReviewsCount": min_reviews_count,
            "facilityIds": facility_ids,
            "hotelTypeIds": hotel_type_ids,
            "chainIds": chain_ids,
            "strictFacilitiesFiltering": strict_facilities_filtering,
            "starRating": star_rating,
            "placeId": place_id
        }

        params = {key: value for key, value in params.items() if value is not None}

        return self.client.get(endpoint, params=params)
