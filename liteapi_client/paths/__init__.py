# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from liteapi_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    HOTELS = "/hotels"
    HOTELS_RATES = "/hotels/rates"
    RATES_PREBOOK = "/rates/prebook"
    RATES_BOOK = "/rates/book"
    BOOKINGS = "/bookings"
    BOOKINGS_BOOKING_ID = "/bookings/{bookingId}"
    DATA_CITIES = "/data/cities"
    DATA_CURRENCIES = "/data/currencies"
    DATA_HOTELS = "/data/hotels"
    DATA_HOTEL = "/data/hotel"
    DATA_COUNTRIES = "/data/countries"
    DATA_IATA_CODES = "/data/iataCodes"
    GUESTS = "/guests"
