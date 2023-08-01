import typing_extensions

from liteapi_client.apis.tags import TagValues
from liteapi_client.apis.tags.search_api import SearchApi
from liteapi_client.apis.tags.book_api import BookApi
from liteapi_client.apis.tags.booking_management_api import BookingManagementApi
from liteapi_client.apis.tags.static_data_api import StaticDataApi
from liteapi_client.apis.tags.guest_and_loyalty_api import GuestAndLoyaltyApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.SEARCH: SearchApi,
        TagValues.BOOK: BookApi,
        TagValues.BOOKING_MANAGEMENT: BookingManagementApi,
        TagValues.STATIC_DATA: StaticDataApi,
        TagValues.GUEST_AND_LOYALTY: GuestAndLoyaltyApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.SEARCH: SearchApi,
        TagValues.BOOK: BookApi,
        TagValues.BOOKING_MANAGEMENT: BookingManagementApi,
        TagValues.STATIC_DATA: StaticDataApi,
        TagValues.GUEST_AND_LOYALTY: GuestAndLoyaltyApi,
    }
)
