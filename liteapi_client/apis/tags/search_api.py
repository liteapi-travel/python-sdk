# coding: utf-8

"""
    liteAPI

    The **liteAPI** can be used to to do the following  Get room rates & availability for a set of hotels Select a specific hotel with room availability and make a booking Manage the bookings - retrieve and cancel existing bookings Get static content for hotels, search hotels by destination  # noqa: E501


"""

from liteapi_client.paths.minimum_rates.get import HotelsGet
from liteapi_client.paths.full_rates.get import HotelsRatesGet


class SearchApi(
    HotelsGet,
    HotelsRatesGet,
):

    pass
