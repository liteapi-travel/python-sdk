# coding: utf-8

"""
    liteAPI

    The **liteAPI** can be used to to do the following  Get room rates & availability for a set of hotels Select a specific hotel with room availability and make a booking Manage the bookings - retrieve and cancel existing bookings Get static content for hotels, search hotels by destination  # noqa: E501

"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "liteapi-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi >= 14.5.14",
    "frozendict ~= 2.3.4",
    "python-dateutil ~= 2.7.0",
    "setuptools >= 21.0.0",
    "typing_extensions ~= 4.3.0",
    "urllib3 ~= 1.26.7",
]

setup(
    name=NAME,
    version=VERSION,
    description="liteAPI",
    author="liteAPI",
    url="https://github.com/liteapi-travel/python-sdk",
    keywords=[    "travel",
    "hotels",
    "api",
    "sdk",
    "booking",
    "vacation",
    "Accommodation",
    "Liteapi",
    "Nuitee"],
    python_requires=">=3.7",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    The **liteAPI** can be used to to do the following  Get room rates &amp; availability for a set of hotels Select a specific hotel with room availability and make a booking Manage the bookings - retrieve and cancel existing bookings Get static content for hotels, search hotels by destination  # noqa: E501
    """
)
