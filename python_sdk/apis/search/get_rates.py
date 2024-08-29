# python_sdk/apis/search/get_rates.py

from typing import List, Dict, Any, Optional
from python_sdk.client import LiteApiClient

class GetRatesApi:
    def __init__(self, client: LiteApiClient):
        self.client = client

    def get_rates(
        self,
        hotel_ids: List[str],
        occupancies: List[Dict[str, Any]],
        checkin: str,
        checkout: str,
        currency: str,
        guest_nationality: str,
        timeout: Optional[float] = 4.0,
        room_mapping: Optional[bool] = False,
        hotel_name: Optional[str] = None,
        country_code: Optional[str] = None,
        city_name: Optional[str] = None,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
        radius: Optional[int] = None,
        iata_code: Optional[str] = None,
        limit: Optional[int] = 200,
        offset: Optional[int] = 0,
        ai_search: Optional[str] = None,
        min_reviews_count: Optional[int] = None,
        min_rating: Optional[float] = None,
        zip_code: Optional[str] = None,
        place_id: Optional[str] = None,
        star_rating: Optional[List[float]] = None,
        hotel_type_ids: Optional[List[int]] = None,
        chain_ids: Optional[List[int]] = None,
        facilities: Optional[List[int]] = None,
        strict_facility_filtering: Optional[bool] = False
    ) -> Dict[str, Any]:
        endpoint = f"{self.client.service_url}/hotels/rates"
        payload = {
            "hotelIds": hotel_ids,
            "occupancies": occupancies,
            "checkin": checkin,
            "checkout": checkout,
            "currency": currency,
            "guestNationality": guest_nationality,
            "timeout": timeout,
            "roomMapping": room_mapping,
            "hotelName": hotel_name,
            "countryCode": country_code,
            "cityName": city_name,
            "latitude": latitude,
            "longitude": longitude,
            "radius": radius,
            "iataCode": iata_code,
            "limit": limit,
            "offset": offset,
            "aiSearch": ai_search,
            "minReviewsCount": min_reviews_count,
            "minRating": min_rating,
            "zip": zip_code,
            "placeId": place_id,
            "starRating": star_rating,
            "hotelTypeIds": hotel_type_ids,
            "chainIds": chain_ids,
            "facilities": facilities,
            "strictFacilityFiltering": strict_facility_filtering
        }

        response = self.client.post(endpoint, data=payload)
        return response
