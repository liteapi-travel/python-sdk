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
        endpoint = f"{self.client.base_url}/hotels/rates"
        payload = {
            "hotelIds": hotel_ids,
            "occupancies": occupancies,
            "checkin": checkin,
            "checkout": checkout,
            "currency": currency,
            "guestNationality": guest_nationality,
            "timeout": timeout,
            "roomMapping": room_mapping,
        }

        # Add optional parameters to the payload if they are provided
        if hotel_name:
            payload["hotelName"] = hotel_name
        if country_code:
            payload["countryCode"] = country_code
        if city_name:
            payload["cityName"] = city_name
        if latitude:
            payload["latitude"] = latitude
        if longitude:
            payload["longitude"] = longitude
        if radius:
            payload["radius"] = radius
        if iata_code:
            payload["iataCode"] = iata_code
        if limit:
            payload["limit"] = limit
        if offset:
            payload["offset"] = offset
        if ai_search:
            payload["aiSearch"] = ai_search
        if min_reviews_count:
            payload["minReviewsCount"] = min_reviews_count
        if min_rating:
            payload["minRating"] = min_rating
        if zip_code:
            payload["zip"] = zip_code
        if place_id:
            payload["placeId"] = place_id
        if star_rating:
            payload["starRating"] = star_rating
        if hotel_type_ids:
            payload["hotelTypeIds"] = hotel_type_ids
        if chain_ids:
            payload["chainIds"] = chain_ids
        if facilities:
            payload["facilities"] = facilities
        if strict_facility_filtering:
            payload["strictFacilityFiltering"] = strict_facility_filtering

        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "X-API-Key": self.client.api_key
        }

        response = self.client.post(endpoint, json=payload, headers=headers)

        return response.json()
