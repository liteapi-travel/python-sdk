# coding: utf-8

# flake8: noqa

"""
    liteAPI

    The **liteAPI** can be used to to do the following  Get room rates & availability for a set of hotels Select a specific hotel with room availability and make a booking Manage the bookings - retrieve and cancel existing bookings Get static content for hotels, search hotels by destination  # noqa: E501


"""

__version__ = "1.0.0"

# import ApiClient
from liteapi_client.api_client import ApiClient

# import Configuration
from liteapi_client.configuration import Configuration

# import exceptions
from liteapi_client.exceptions import LiteApiException
from liteapi_client.exceptions import ApiAttributeError
from liteapi_client.exceptions import ApiTypeError
from liteapi_client.exceptions import ApiValueError
from liteapi_client.exceptions import ApiKeyError
from liteapi_client.exceptions import ApiException
