# coding: utf-8

"""
    liteAPI

    The **liteAPI** can be used to to do the following  Get room rates & availability for a set of hotels Select a specific hotel with room availability and make a booking Manage the bookings - retrieve and cancel existing bookings Get static content for hotels, search hotels by destination  # noqa: E501


"""

from liteapi_client.paths.data_cities.get import DataCitiesGet
from liteapi_client.paths.data_countries.get import DataCountriesGet
from liteapi_client.paths.data_currencies.get import DataCurrenciesGet
from liteapi_client.paths.data_hotel.get import DataHotelGet
from liteapi_client.paths.data_hotels.get import DataHotelsGet
from liteapi_client.paths.data_iata_codes.get import DataIataCodesGet


class StaticDataApi(
    DataCitiesGet,
    DataCountriesGet,
    DataCurrenciesGet,
    DataHotelGet,
    DataHotelsGet,
    DataIataCodesGet,
):

    pass
