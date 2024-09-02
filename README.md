
# LiteAPI Python SDK

A Python SDK for interacting with the LiteAPI platform.

<h1 style="font-weight: 500;">liteAPI SDK</h1>

# Table of Contents
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [Installing](#installing)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Testing](#Testing)
  - [Build and publish the package](#Build-and-publish-the-package)
- [Usage](#usage)
- [Static data](#static-data)
  - [List of cities](#list-of-cities)
  - [List of Countries](#list-of-countries)
  - [List of available currencies](#list-of-available-currencies)
  - [List of hotels](#list-of-hotels)
  - [Hotel details](#hotel-details)
  - [IATA code list](#iata-code-list)
- [Booking flow](#booking-flow)
  - [Search](#search)
    - [Retrieve rates for hotels](#hotel-full-rates-availability)
  - [Book](#book)
    - [Hotel rate prebook](#hotel-rate-prebook)
    - [Hotel rate book](#hotel-rate-book)
  - [Booking management](#booking-management)
    - [Booking retrieve](#booking-retrieve)
    - [Booking cancel](#booking-cancel)
  - [Vouchers and loyalty](#vouchers)
    - [Vouchers](#voucher-details)
    - [VoucherID](#voucher-details)
    - [Loyalty Program](#loyalty-program)
- [Example Project](#example-project)

# Introduction
[liteAPI](https://www.liteapi.travel/) is an innovative and robust collection of infrastructure APIs that cater to the travel industry. It is designed to empower developers, offering them the fastest way to build and launch comprehensive travel applications.

At the heart of LiteAPI's power is its extensive network of over 2 million properties worldwide. By incorporating LiteAPI into an app, developers can effortlessly tap into the vast inventory, allowing users to search and book accommodations at these properties.

But that's not all. With LiteAPI, monetization is made even more simple. Developers can generate revenue through their hospitality products by selling accommodations from LiteAPI's broad portfolio of properties. This means that not only can developers launch their products quickly, they can also start generating profits in no time.

LiteAPI opens up a range of powerful functions for travel and hospitality applications. Its features include:

<h3 style="font-weight: 500; display:inline">Hotel Search:</h3> Developers can incorporate a robust search function that allows users to find hotels based on their preferred destination. This can help users discover accommodations that suit their travel plans.
<br><br>
<h3 style="font-weight: 500; display:inline">Static Content for Hotels:</h3> LiteAPI also provides access to static content for hotels, including descriptions, images, and amenity details. This is essential for developers to present comprehensive and accurate information to the end users, aiding their decision-making process.
<br><br>
<h3 style="font-weight: 500; display:inline">Room Rates & Availability:</h3> One of the most significant features of LiteAPI is the ability to pull data on room rates and availability for a selected set of hotels. This feature ensures users have real-time, accurate information to assist in their booking decisions.
<br><br>
<h3 style="font-weight: 500; display:inline">Hotel Booking:</h3> Beyond just providing information, LiteAPI also allows developers to integrate a seamless booking function. Users can select a specific hotel with room availability and proceed to make a booking directly within the app.
<br><br>
<h3 style="font-weight: 500; display:inline">Booking Management:</h3> With LiteAPI, managing bookings becomes a straightforward task. The booking management functions allow for the tracking and management of all bookings made through the app, ensuring users can keep track of their travel plans.
<br><br>
<h3 style="font-weight: 500; display:inline">Booking Retrieval and Cancellation:</h3> Lastly, LiteAPI offers the capability to retrieve and cancel existing bookings. This added flexibility is crucial for users who might need to alter their travel plans.
<br><br>
<h3 style="font-weight: 500; display:inline">Vouchers:</h3> LiteAPI allows developers to manage and retrieve vouchers, adding an extra layer of value to users by offering discounts or special offers through the app.
<br><br>
<h3 style="font-weight: 500; display:inline">Loyalty Program:</h3> A comprehensive loyalty system within liteAPI, which includes guest tracking, loyalty points accrual, and retrieval of guest booking history and information via a unique guestId.
<br><br>
All these features make LiteAPI a comprehensive solution for travel app development, offering a plethora of functionalities, from search and booking to management and cancellation. Developers can harness these powerful tools to create high-quality, user-friendly travel applications.
<br><br>

Don't have an account yet?  Sign Up [Here](https://dashboard.liteapi.travel/register/).


# Installing

## Requirements

Python &gt;&#x3D;3.7

## Installation

To install the package, simply run the following commands:

```sh
pip install git+https://github.com/liteapi-travel/python-sdk.git
```

## Testing

```
python3 -m unittest discover tests
```

---

## Build and publish the package

```bash
pip install setuptools wheel
python3 setup.py sdist bdist_wheel
pip install twine
twine upload dist/*
```

# Usage

After you have installed the LiteAPI package, you need to configure it with your API key. The API key is available in the [liteAPI Dashboard](https://dashboard.liteapi.travel/apikeys/). Here's the step to add the API key to the package.

```python
from liteapi import LiteApi
cls.api_key =  # Set up with a real API key and other necessary setup
cls.api = LiteApi(cls.api_key)
```


# Static data

Static data can be directly fetched from the functions below. Alternatively, LiteAPI also provides an option to download static data directly from the [Github URL](STATICDATA.md).

To fetch static data from the functions, you need to create an instance of the StaticDataApi as follows:

```python
    def setUpClass(cls):
        cls.api = LiteApi(cls.api_key)

        cls.test_hotel_id = "lp1897"
  
    def test_get_countries(self):
        response = self.api.get_countries()
        self.assertEqual(response["status"], "success")
        self.assertIn("data", response)
```
## List of cities

The get_cities function returns a list of city names from a specific country. The country codes must be in ISO-2 format. To get the country codes in ISO-2 for all countries please use the getCountries function. 

*  <h4 style="color:#9155fd; font-weight: 800;"> Example :</h4>
```python
response = self.api.get_cities_by_country_code("US")
```
*  <h4 style="color:#9155fd; font-weight: 800;"> Parameters :</h4>


| Name            | Type       | Description                                | Notes      |
| --------------- | ---------- | ------------------------------------------ | ---------- |
| **countryCode** | **String** | Country code in iso-2 format (example: US) | [required] |
| **timeout**     | **Float**  | Request timeout in seconds (default: 4.0)	| [optional] |

*  <h4 style="color:#9155fd; font-weight: 800;"> Return type :</h4>

An array of city objects containing the following properties:

| Field    | Type       | Description           |
| -------- | ---------- | --------------------- |
| **city** | **String** | The name of the city. |

<br>

## List of Countries

The get_countries function returns the list of countries available along with its ISO-2 code.

*  <h4 style="color:#9155fd; font-weight: 800;"> Example :</h4>
```python
response = self.api.get_countries()
```
*  <h4 style="color:#9155fd; font-weight: 800;"> Parameters :</h4>

| Name            | Type       | Description                                | Notes      |
| --------------- | ---------- | ------------------------------------------ | ---------- |
| **timeout**     | **Float**  | Request timeout in seconds (default: 4.0)	| [optional] |

*  <h4 style="color:#9155fd; font-weight: 800;"> Return type :</h4>

An array of country objects containing the following properties:

| Field    | Type       | Description                       |
| -------- | ---------- | --------------------------------- |
| **code** | **String** | The country code in iso-2 format. |
| **name** | **String** | The name of the country.          |

<br>

## List of available currencies

The get_currencies function returns all available currency codes along with its name and the list of supported countries that the currency applies to.

*  <h4 style="color:#9155fd; font-weight: 800;"> Example :</h4>
```python
response = self.api.get_currencies()
```
*  <h4 style="color:#9155fd; font-weight: 800;"> Parameters :</h4>

| Name            | Type       | Description                                | Notes      |
| --------------- | ---------- | ------------------------------------------ | ---------- |
| **timeout**     | **Float**  | Request timeout in seconds (default: 4.0)	| [optional] |

*  <h4 style="color:#9155fd; font-weight: 800;"> Return type :</h4>

An array of currency objects containing the following properties:

| Name          | Type       | Description                                       |
| ------------- | ---------- | ------------------------------------------------- |
| **code**      | **String** | The currency code.                                |
| **currency**  | **String** | The name of the currency.                         |
| **countries** | **Array**  | An array of countries where the currency is used. |

<br>

## List of hotels

The get_hotels function returns a list of hotels available based on different search criteria. The minimum required information is the country code in ISO-2 format.

*  <h4 style="color:#9155fd; font-weight: 800;"> Example :</h4>
```python
response = self.api.get_hotels("US", "New York")
```

*  <h4 style="color:#9155fd; font-weight: 800;"> Parameters :</h4>

| Name            | Type       | Description                                                         | Notes      |
| --------------- | ---------- | ------------------------------------------------------------------- | ---------- |
| **countryCode** | **String** | country code ISO-2 code - example (US)                              | [required] |
| **cityName**    | **String** | name of the city                                                    | [optional] |
| **hotel_name**  | **String** | Name of the hotel	                                                 | [optional] |
| **offset**      | **Integer** | specifies the number of rows to skip before starting to return rows | [optional] |
| **limit**       | **Integer** | limit number of results (max 1000)                                 | [optional] |
| **longitude**   | **String** | longitude geo coordinates                                           | [optional] |
| **latitude**    | **String** | latitude geo coordinates                                            | [optional] |
| **radius**      | **Integer** | Search radius in meters                                            | [optional] |
| **ai_search**   | **String** | AI-based search paramete                                            | [optional] |
| **timeout**     | **Float** | Request timeout in seconds                                           | [optional] |
| **zip_code**    | **String** | Postal code filter                                                  | [optional] |
| **min_rating**  | **Float** | Minimum rating of hotels to be returned                              | [optional] |
| **min_reviews_count** | **Integer** | Minimum number of reviews for the hotels                     | [optional] |
| **facility_ids** | **String** | Facility IDs to filter hotels	                                     | [optional] |
| **hotel_type_ids** | **String** | Hotel type IDs to filter hotels                                  | [optional] |
| **chain_ids** | **String** | Hotel chain IDs to filter hotels	                                     | [optional] |
| **strict_facilities_filtering** | **Bool** | Strictly filter by facil                              | [optional] |
| **star_rating** | **String** | Star rating of hotels to filter by	                                 | [optional] |
| **place_id** | **String** | Place ID for specific searches	                                     | [optional] |



*  <h4 style="color:#9155fd; font-weight: 800;"> Return type :</h4>

An array of hotel objects containing the following properties:  

| Name                 | Type       | Description                                        |
| -------------------- | ---------- | -------------------------------------------------- |
| **id**               | **String** | The unique identifier of the hotel.                |
| **name**             | **String** | The name of the hotel.                             |
| **hotelDescription** | **String** | The description of the hotel.                      |
| **currency**         | **String** | The currency used in the hotel.                    |
| **country**          | **String** | The country code of the hotel.                     |
| **city**             | **String** | The city where the hotel is located.               |
| **latitude**         | **number** | The latitude coordinates of the hotel's location.  |
| **longitude**        | **number** | The longitude coordinates of the hotel's location. |
| **address**          | **String** | The address of the hotel.                          |
| **zip**              | **String** | The postal code of the hotel.                      |
| **main_photo**       | **String** | The URL of the main photo of the hotel.            |
| **stars**            | **number** | The star rating of the hotel.                      |

<br>

## Hotel details

The get_hotel_details function returns all the static contents details of a hotel or property when given a hotel ID. The static content includes name, description, address, amenities, cancellation policies, images and more.

*  <h4 style="color:#9155fd; font-weight: 800;"> Example :</h4>
```python
response = self.api.get_hotel_details(self.test_hotel_id)
```
*  <h4 style="color:#9155fd; font-weight: 800;"> Parameters :</h4>
| Name        | Type       | Description          | Notes      |
| ----------- | ---------- | -------------------- | ---------- |
| **hotelId** | **String** | Unique ID of a hotel | [required] |
| **timeout** | **Float**  | Request timeout in seconds (default: 4.0)	 | [optional] |

*  <h4 style="color:#9155fd; font-weight: 800;"> Return type :</h4>

| Name                                                              | Type        | Description                                                                          |
| ----------------------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------ |
| **id**                                                            | **String**  | The unique identifier of the hotel.                                                  |
| **name**                                                          | **String**  | The name of the hotel.                                                               |
| **hotelDescription**                                              | **String**  | The description of the hotel.                                                        |
| **checkinCheckoutTimes**                                          | **Object**  | An object containing the check-in and check-out times of the hotel.                  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **checkout**     | **String**  | The check-out time of the hotel.                                                     |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **checkin**      | **String**  | The check-in time of the hotel.                                                      |
| **hotelImages**                                                   | **Array**   | An array of hotel image objects containing the following properties:                 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **url**          | **String**  | The URL of the hotel image.                                                          |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **thumbnailUrl**       | **String**  | The thumbnail URL of the hotel image.                                                |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **caption**      | **String**  | The caption of the hotel image.                                                      |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **order**        | **String**  | The order of the hotel image (null if not applicable).                               |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **defaultImage** | **boolean** | Indicates whether the hotel image is the default image or not.                       |
| **currency**                                                      | **String**  | The currency used in the hotel.                                                      |
| **country**                                                       | **String**  | The country code of the hotel.                                                       |
| **city**                                                          | **String**  | The city where the hotel is located.                                                 |
| **starRating**                                                    | **number**  | The star rating of the hotel.                                                        |
| **location**                                                      | **Object**  | An object containing the latitude and longitude coordinates of the hotel's location. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **latitude**     | **number**  | The latitude coordinate of the hotel's location.                                     |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **longitude**    | **number**  | The longitude coordinate of the hotel's location.                                    |
| **address**                                                       | **String**  | The address of the hotel.                                                            |
| **zip**                                                           | **String**  | The postal code of the hotel.                                                        |
| **chainId**                                                       | **String**  | The unique identifier of the hotel chain.                                            |
| **hotelFacilities**                                               | **Array**   | An array of hotel facilities offered by the hotel.                                   |

<br>

## IATA code list

The get_iata_codes function returns the IATA (International Air Transport Association) codes for all available airports along with the name of the airport, geographical coordinates and country code in ISO-2 format.


*  <h4 style="color:#9155fd; font-weight: 800;"> Example :</h4>
```python
response = self.api.get_iata_codes()
```
*  <h4 style="color:#9155fd; font-weight: 800;"> Parameters :</h4>

| Name        | Type       | Description                                 | Notes      |
| ----------- | ---------- | ------------------------------------------- | ---------- |
| **timeout** | **Float**  | Request timeout in seconds (default: 4.0)	 | [optional] |

*  <h4 style="color:#9155fd; font-weight: 800;"> Return type :</h4>

An array of IATA objects with the following properties:

| Name            | Type       | Description                            |
| --------------- | ---------- | -------------------------------------- |
| **code**        | **String** | The IATA code.                         |
| **name**        | **String** | The name of the IATA.                  |
| **latitude**    | **number** | The latitude coordinates of the IATA.  |
| **longitude**   | **number** | The longitude coordinates of the IATA. |
| **countryCode** | **String** | The country code of the IATA.          |

<br>

# Booking flow

liteAPI offers a comprehensive and simple way to implement Hotel Booking flow. The booking flow consists of 3 sections: Search, Book, and 
booking management.

```python
    def setUpClass(cls):
        cls.api = LiteApi(cls.api_key)

        cls.test_offer_id = "offerID"
        cls.test_booking_id = "0QYXiyJGP"
     
    def test_cancel_booking(self):
        response = self.api.cancel_booking(self.test_booking_id)
        self.assertEqual(response["status"], "success")
        self.assertIn("data", response)
```

## Search

To access the search functionality and retrieve available hotels, you need to create an instance of the SearchApi as follows:

### Retrieve rates for hotels
------
This endpoint allows developers to retrieve detailed rate information for hotels, supporting multi-room bookings. By making a POST request with the required parameters, you receive an array of offers, each containing comprehensive rate details. This endpoint is essential for providing users with detailed booking options, including pricing and room specifications.

The request requires an array of hotelIds (up to 200 per request), checkin, checkout, and an array of occupancies objects. Each occupancy object specifies the number of adults and ages of children for each room requested.

*  <h4 style="color:#9155fd; font-weight: 800;"> Example :</h4>
```python
response = self.api.get_full_rates({
            "checkin": "2024-12-01",
            "checkout": "2024-12-05",
            "hotelIds": [self.test_hotel_id],
            "occupancies": [{"adults": 2, "children": []}],
            "guestNationality": "US",
            "currency": "USD",
            "roomMapping": True
        })
```

*  <h4 style="color:#9155fd; font-weight: 800;"> Parameters :</h4>

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hotelIds** | **array of Strings**| List of hotelIds | [required]
 **checkin** | **String**| Check in data in YYYY-MM-DD format | [required]
 **checkout** | **String**| Check out data in YYYY-MM-DD format | [required]
 **currency** | **String**| Currency code - example (USD) | [required]
 **guestNationality** | **String**| Guest nationality ISO-2 code - example (SG) | [required]
 **adults** | **Integer**| Number of adult guests staying | [required]
 **children** | **array of Integers**| Number of children staying if any | [optional] 
 **guestId** | **String**| Unique traveler ID if available | [optional] 
  **timeout** | **Float**| Request timeout in seconds (default: 4.0).	 | [optional] 

*  <h4 style="color:#9155fd; font-weight: 800;"> Return type :</h4>

An array of hotel full rates with the following properties:

| Name         | Type   | Description                                      |
| ------------ | ------ | ------------------------------------------------ |
| **roomTypeId** | **String** | The ID of the room type.                                                                                |
| **supplier**   | **String** | The name of the supplier.                                                                               |
| **supplierId** | **number** | The ID of the supplier.                                                                                 |
| **rates**      | **Array**  | An array of rate objects containing the pricing and details for each rate within the room type.        |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **rateId**        | **String** | The ID of the rate.                                                                                   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **name**          | **String** | The name of the rate.                                                                                 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **maxOccupancy** | **number** | The maximum occupancy of the room.                                                                     |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **boardType**     | **String** | The type of board included (e.g., Bed Only).                                                           |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **boardName**     | **String** | The name of the board (e.g., Bed Only).                                                                 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **priceType**     | **String** | The type of pricing (e.g., commission).                                                                 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **commission**    | **Array**  | An array of commission objects containing the commission amount and currency.                         |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **retailRate**    | **Object** | An object containing the retail rate information, including total price, MSP (Marked Selling Price), and taxes and fees. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **total**         | **Array**  | An array of total price objects containing the amount and currency.                                    |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **msp**           | **Array**  | An array of MSP (Marked Selling Price) objects containing the amount and currency.                     |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **taxesAndFees**  | **Array** | An array of taxes and fees objects containing information about included or additional charges.         |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **cancellationPolicies** | **Object** | An object containing cancellation policy information.                                                   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **cancelPolicyInfos** | **Array**  | An array of cancellation policy info objects containing information about cancellation time, amount, currency, and type. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **hotelRemarks**      | **Array** | An array of hotel remarks.                                                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **refundableTag**      | **String** | The tag indicating if the rate is refundable or non-refundable.                                          |


<br>

## Book

To perform pre booking and booking operations, you need to create an instance of the BookApi as follows:

### Hotel rate prebook
------

This endpoint is used to generate a checkout session for a specific offerId. The input to the endpoint is the specific offerId coming from Retrieve rates for hotels endpoint.
The response will include a prebookId which is used to confirm the booking in the next step.
The usePaymentSdk parameter is used to determine if the payment form will be displayed using the client-side Payment SDK or not.
*  <h4 style="color:#9155fd; font-weight: 800;"> Example :</h4>
```python
 response = self.api.retrieve_booking(self.test_booking_id)
```
*  <h4 style="color:#9155fd; font-weight: 800;"> Parameters :</h4>

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**offer_id** | **String**| Offer ID retrieved from the get_full_rates response| [required]
**use_payment_sdk** | **Bool**| Boolean to indicate whether to use the payment SDK.| [required]
**rvoucher_code** | **String**| Voucher code for discounts (if available).| [optional]

*  <h4 style="color:#9155fd; font-weight: 800;"> Return type :</h4>

An object containing prebook information and room type details.                      

| Name                      | Type   | Description                                                                                            |
| ------------------------- | ------ | ------------------------------------------------------------------------------------------------------ |
| **prebookId**        | **String** | The ID of the prebook.                                                                                |
| **hotelId**          | **String** | The ID of the hotel.                                                                                  |
| **currency**         | **String** | The currency used for pricing.                                                                         |
| **termsAndConditions** | **String** | The terms and conditions (if available).                                                               |
| **roomTypes**        | **Array**  | An array of room type objects containing the following properties:                                    |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **rates**      | **Array**  | An array of rate objects containing pricing and details for each rate within the room type.          |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **rateId**        | **String** | The ID of the rate.                                                                                    |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **name**          | **String** | The name of the rate.                                                                                  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **maxOccupancy** | **number** | The maximum occupancy of the room.                                                                      |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **boardType**     | **String** | The type of board included (e.g., Bed Only).                                                            |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **boardName**     | **String** | The name of the board (e.g., Bed Only).                                                                  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **priceType**     | **String** | The type of pricing (e.g., commission).                                                                  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **commission**    | **Object**  | An array of commission objects containing the commission amount and currency.                          |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **retailRate**    | **Object** | An object containing the retail rate information, including total price, MSP (Marked Selling Price), and taxes and fees. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **total**         | **Object**   | An array of total price objects containing the amount and currency.                                     |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **msp**           | **Object**   | An array of MSP (Marked Selling Price) objects containing the amount and currency.                      |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **taxesAndFees**  | **Object**    | An array of taxes and fees objects containing information about included or additional charges.          |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **cancellationPolicies** | **Object** | An object containing cancellation policy information.                                                    |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **cancelPolicyInfos** | **Object** | An array of cancellation policy info objects containing information about cancellation time, amount, and type. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **hotelRemarks**      | **Array**  | An array of hotel remarks.                                                                             |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **refundableTag**      | **String** | The tag indicating if the rate is refundable or non-refundable.                                         |
| **msp**                   | **number** | The Marked Selling Price (MSP) for the prebook.                                                         |
| **commission**            | **number** | The commission amount for the prebook.                                                                  |
| **price**                 | **number** | The price of the prebook.                                                                              |
| **priceType**             | **String** | The type of pricing (e.g., commission).                                                                 |
| **priceDifferencePercent**| **number** | The percentage difference between the retail rate and the Marked Selling Price (MSP).                   |
| **cancellationChanged**   | **boolean** | Indicates if there were changes to the cancellation policy.                                             |
| **boardChanged**          | **boolean** | Indicates if there were changes to the board type.                                                      |
| **supplier**              | **String** | The name of the supplier.                                                                              |
| **supplierId**            | **number** | The ID of the supplier.                                                                                |


<br>

### Hotel rate book
------

This API confirms a booking when the prebookId and the rate Id from the prebook stage along with the guest and payment information are passed.

The guest information is an object that should include the guest first name, last name and email.

The payment information can be two different options:

TRANSACTION method: when using the Payment SDK, you should use this method and provide the relevant transactionId to confirm.
ACC_CREDIT_CARD, WALLET, NONE for all other usages. See our docs for more details.
The response will confirm the booking along with a booking Id and a hotel confirmation code. It will also include the booking details including the dates, price and the cancellation policies.


*  <h4 style="color:#9155fd; font-weight: 800;"> Example :</h4>

```python
response = self.api.book({"offerId": self.test_offer_id})
```

*  <h4 style="color:#9155fd; font-weight: 800;"> Parameters :</h4>

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**prebookId** | **String**| prebook id retrieved from prebook response| [required]
**holder** | **Object**| An object containing the guest's details (first name, last name, email) | [required]
**holderName** | **String**| name of the cardholder	| [required]
**guests** | **Array**| List of guest objects containing guest details. | [required]
**payment_method** | **String**| Payment method, either "CREDIT_CARD" or "STRIPE_TOKEN" | [required]
**transaction_id** | **String**| Transaction ID or Stripe token (required if payment method is "STRIPE_TOKEN") | [optional]
**voucher_code** | **String**| Voucher code for discounts (if available) | [required]


*  <h4 style="color:#9155fd; font-weight: 800;"> Return type :</h4>

An object containing booking information and room details.   


| Name                      | Type    | Description                          |
| ------------------------- | ------- | ------------------------------------ |
| **bookingId**             | **String**  | The ID of the booking.               |
| **clientReference**       | **String**  | The client reference.                |
| **supplierBookingId**     | **String**  | The supplier booking ID.             |
| **supplierBookingName**   | **String**  | The supplier booking name.           |
| **supplier**              | **String**  | The supplier.                        |
| **supplierId**            | **number**  | The ID of the supplier.              |
| **status**                | **String**  | The status of the booking.           |
| **hotelConfirmationCode** | **String**  | The hotel confirmation code.         |
| **checkin**               | **String**  | The check-in date.                   |
| **checkout**              | **String**  | The check-out date.                  |
| **hotel**                 | **object**  | An object containing hotel details.  |
| **bookedRooms**           | **array**   | An array of booked room objects.     |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **roomType**      | **object**  | An object containing room type details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **adults**        | **number**  | The number of adults.           |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **children**      | **number**  | The number of children.         |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **rate**          | **object**  | An object containing rate details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **maxOccupancy**      | **number** | The maximum occupancy.           |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **retailRate**        | **object** | An object containing the retail rate information, including total price. |
| **guestInfo**             | **object**  | An object containing guest details.  |
| **createdAt**             | **String**  | The creation date of the booking.    |
| **cancellationPolicies**  | **object**  | An object containing cancellation policies information.
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **cancelPolicyInfos** | **Object** | An array of cancellation policy info objects containing information about cancellation time, amount, and type. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **hotelRemarks**      | **Array**  | An array of hotel remarks.                                                                             |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **refundableTag**      | **String** | The tag indicating if the rate is refundable or non-refundable.
| **price**                 | **number**  | The price of the booking.            |
| **msp**                   | **number**  | The MSP (Merchant Service Provider) price. |
| **commission**            | **number**  | The commission amount.               |
| **currency**              | **String**  | The currency of the booking.         |


<br>

## Booking management

To manage bookings to perform various operations such as retrieving a list of bookings, fetching details of a specific booking, and cancelling a booking, you need to create an instance of the BookingManagementApi instance as follows:

### Booking retrieve
------

The retrieved_booking function returns the status and the details of a specific booking Id.

*  <h4 style="color:#9155fd; font-weight: 800;"> Example :</h4>
```python
response = self.api.retrieve_booking(self.test_booking_id)
```
*  <h4 style="color:#9155fd; font-weight: 800;"> Parameters :</h4>


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bookingId** | **String** | The Booking Id that needs to be retrieved | [required]


*  <h4 style="color:#9155fd; font-weight: 800;"> Return type :</h4>

An object containing booking information and room details.   

| Name                  | Type   | Description                      |
| --------------------- | ------ | -------------------------------- |
| **bookingId**         | **String** | The booking ID.                  |
| **clientReference**   | **String** | The client reference.            |
| **status**            | **String** | The booking status.              |
| **hotelConfirmationCode** | **String** | The hotel confirmation code.    |
| **checkin**           | **String** | The check-in date.               |
| **checkout**          | **String** | The check-out date.              |
| **hotel**             | **object** | An object containing hotel details. |
| **bookedRooms**       | **array**  | An array of booked room objects. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **roomType**      | **object**  | An object containing room type details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **adults**        | **number**  | The number of adults.           |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **children**      | **number**  | The number of children.         |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **rate**          | **object**  | An object containing rate details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **maxOccupancy**      | **number** | The maximum occupancy.           |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **boardType**    | **String** | The board type.              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **boardName**    | **String** | The board name.              |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **retailRate**        | **object** | An object containing the retail rate information, including total price. |
| **guestInfo**         | **object** | An object containing guest information. |
| **createdAt**         | **String** | The creation date of the booking. |
| **cancellationPolicies** | **object** | An object containing cancellation policy details. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **cancelPolicyInfos** | **Object** | An array of cancellation policy info objects containing information about cancellation time, amount, and type. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **hotelRemarks**      | **Array**  | An array of hotel remarks.                                                                             |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **refundableTag**      | **String** | The tag indicating if the rate is refundable or non-refundable.
| **currency**          | **String** | The currency code.               |
| **price**             | **number** | The price of the booking.        |



<br>

### Booking cancel
------

The cancel_booking function is used to request a cancellation of an existing confirmed booking. Cancellation policies and conditions will be used to determine the success of the cancellation. For example a booking with non-refundable (NRFN) tag or a booking with a cancellation policy that was requested past the cancellation date will not be able to cancel the confirmed booking.

*  <h4 style="color:#9155fd; font-weight: 800;"> Example :</h4>
```python
response = self.api.cancel_booking(self.test_booking_id)
```
*  <h4 style="color:#9155fd; font-weight: 800;"> Parameters :</h4>

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bookingId** | **String** | The booking Id of the booking you would like to cancel. |  [required]



*  <h4 style="color:#9155fd; font-weight: 800;"> Return type :</h4>

| Name             | Type   | Description                 |
| ---------------- | ------ | --------------------------- |
| **bookingId**    | **String** | The booking ID.             |
| **status**       | **String** | The booking status.         |
| **cancellation_fee** | **number** | The cancellation fee.       |
| **refund_amount**    | **number** | The refund amount.          |
| **currency**     | **String** | The currency of the booking. |

<br>


# Vouchers and loyalty

LiteAPI provides straightforward access to voucher details, including codes and discounts, along with current loyalty program status and cashback rates.

```python
    def setUpClass(cls):
        cls.api = LiteApi(cls.api_key)

        cls.test_voucher_id = "68"

     def test_get_voucher_by_id(self):
        response = self.api.get_voucher_by_id(self.test_voucher_id)
        self.assertEqual(response["status"], "success")
        self.assertIn("data", response)
```

## Vouchers

The getVouchers function retrieves a list of all available vouchers. This endpoint provides details such as the voucher code, discount type and value, validity period, and other relevant information.

*  <h4 style="color:#9155fd; font-weight: 800;"> Example :</h4>
```python
response = self.api.get_vouchers()
```
*  <h4 style="color:#9155fd; font-weight: 800;"> Parameters :</h4>

This function does not require any parameters.

*  <h4 style="color:#9155fd; font-weight: 800;"> Return type :</h4>

An array of city objects containing the following properties:

| Field    | Type       | Description           |
| -------- | ---------- | --------------------- |
| **voucherCode** | **String** | The code of the voucher |
| **discount** | **Object** | An object containing discount details (type, value) |
| **validity** | **Object** | An object with start and end date for voucher usage |

<br>

## VoucherID

The getVoucherById function retrieves details of a specific voucher by its ID. This includes the voucher code, discount details, usage limits, and more.

*  <h4 style="color:#9155fd; font-weight: 800;"> Example :</h4>
```python
response = self.api.get_voucher_by_id(self.test_voucher_id)
```
*  <h4 style="color:#9155fd; font-weight: 800;"> Parameters :</h4>

| Name            | Type       | Description                                | Notes      |
| --------------- | ---------- | ------------------------------------------ | ---------- |
| **voucher_id**     | **Integer**  | The ID of the voucher to retrieve.		| [required] |

*  <h4 style="color:#9155fd; font-weight: 800;"> Return type :</h4>

An array of country objects containing the following properties:

| Field    | Type       | Description                       |
| -------- | ---------- | --------------------------------- |
| **voucherCode** | **String** | The code of the voucher |
| **discount** | **Object** | An object containing discount details |
| **usageLimits** | **Object** | An object with usage limit details |
| **validity** | **Object** | An object with start and end date for voucher usage |


<br>

## Loyalty Program

The getLoyalty function retrieves information about current loyalty program settings, including status and cashback rates.

*  <h4 style="color:#9155fd; font-weight: 800;"> Example :</h4>
```python
response = self.api.get_loyalty()
```
*  <h4 style="color:#9155fd; font-weight: 800;"> Parameters :</h4>

This function does not require any parameters.

*  <h4 style="color:#9155fd; font-weight: 800;"> Return type :</h4>

An array of currency objects containing the following properties:

| Name          | Type       | Description                                       |
| ------------- | ---------- | ------------------------------------------------- |
| **status**      | **String** | The current status of the loyalty program (active/inactive)   |
| **cashbackRate** | **Float**  | The cashback rate offered by the loyalty program.|

<br>


# Example Project
To see an example project demonstrating how to integrate the SDK, visit [liteAPI-python-sdk-example](https://github.com/liteapi-travel/python-sdk-examples)
