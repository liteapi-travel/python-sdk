import typing_extensions

from liteapi_client.paths import PathValues
from liteapi_client.apis.paths.hotels import Hotels
from liteapi_client.apis.paths.hotels_rates import HotelsRates
from liteapi_client.apis.paths.rates_prebook import RatesPrebook
from liteapi_client.apis.paths.rates_book import RatesBook
from liteapi_client.apis.paths.bookings import Bookings
from liteapi_client.apis.paths.bookings_booking_id import BookingsBookingId
from liteapi_client.apis.paths.data_cities import DataCities
from liteapi_client.apis.paths.data_currencies import DataCurrencies
from liteapi_client.apis.paths.data_hotels import DataHotels
from liteapi_client.apis.paths.data_hotel import DataHotel
from liteapi_client.apis.paths.data_countries import DataCountries
from liteapi_client.apis.paths.data_iata_codes import DataIataCodes
from liteapi_client.apis.paths.guests import Guests

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.HOTELS: Hotels,
        PathValues.HOTELS_RATES: HotelsRates,
        PathValues.RATES_PREBOOK: RatesPrebook,
        PathValues.RATES_BOOK: RatesBook,
        PathValues.BOOKINGS: Bookings,
        PathValues.BOOKINGS_BOOKING_ID: BookingsBookingId,
        PathValues.DATA_CITIES: DataCities,
        PathValues.DATA_CURRENCIES: DataCurrencies,
        PathValues.DATA_HOTELS: DataHotels,
        PathValues.DATA_HOTEL: DataHotel,
        PathValues.DATA_COUNTRIES: DataCountries,
        PathValues.DATA_IATA_CODES: DataIataCodes,
        PathValues.GUESTS: Guests,
    }
)

path_to_api = PathToApi(
    {
        PathValues.HOTELS: Hotels,
        PathValues.HOTELS_RATES: HotelsRates,
        PathValues.RATES_PREBOOK: RatesPrebook,
        PathValues.RATES_BOOK: RatesBook,
        PathValues.BOOKINGS: Bookings,
        PathValues.BOOKINGS_BOOKING_ID: BookingsBookingId,
        PathValues.DATA_CITIES: DataCities,
        PathValues.DATA_CURRENCIES: DataCurrencies,
        PathValues.DATA_HOTELS: DataHotels,
        PathValues.DATA_HOTEL: DataHotel,
        PathValues.DATA_COUNTRIES: DataCountries,
        PathValues.DATA_IATA_CODES: DataIataCodes,
        PathValues.GUESTS: Guests,
    }
)
