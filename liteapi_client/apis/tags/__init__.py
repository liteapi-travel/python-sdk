# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from liteapi_client.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    SEARCH = "search"
    BOOK = "book"
    BOOKING_MANAGEMENT = "booking management"
    STATIC_DATA = "static data"
    GUEST_AND_LOYALTY = "guest and loyalty"
