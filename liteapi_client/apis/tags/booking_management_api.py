# coding: utf-8

"""
    liteAPI

    The **liteAPI** can be used to to do the following  Get room rates & availability for a set of hotels Select a specific hotel with room availability and make a booking Manage the bookings - retrieve and cancel existing bookings Get static content for hotels, search hotels by destination  # noqa: E501


"""

from liteapi_client.paths.bookings_booking_id.get import BookingsBookingIdGet
from liteapi_client.paths.bookings_booking_id.put import BookingsBookingIdPut
from liteapi_client.paths.bookings.get import BookingsGet


class BookingManagementApi(
    BookingsBookingIdGet,
    BookingsBookingIdPut,
    BookingsGet,
):

    pass
