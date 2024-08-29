import unittest
from python_sdk.client import Client

class TestPythonSDK(unittest.TestCase):

    def setUp(self):
        self.client = Client(api_key="your_api_key")  # Replace with actual API key

    def test_get_hotels(self):
        response = self.client.apis.hotel.get_hotels()
        self.assertIn("data", response)
        self.assertTrue(len(response["data"]) > 0)
        print(response)

    def test_get_hotel_details(self):
        response = self.client.apis.hotel.get_hotel_details(hotel_id="lp4c2bf")
        self.assertIn("data", response)
        self.assertEqual(response["data"]["id"], "lp4c2bf")
        print(response)

    def test_get_hotel_reviews(self):
        response = self.client.apis.hotel.get_hotel_reviews(hotel_id="lp4c2bf")
        self.assertIn("data", response)
        self.assertTrue(len(response["data"]) > 0)
        print(response)

    def test_get_cities_by_country_code(self):
        response = self.client.apis.city.get_cities_by_country_code(country_code="AE")
        self.assertIn("data", response)
        self.assertTrue(len(response["data"]) > 0)
        print(response)

    def test_get_countries(self):
        response = self.client.apis.country.get_countries()
        self.assertIn("data", response)
        self.assertTrue(len(response["data"]) > 0)
        print(response)

    def test_get_currencies(self):
        response = self.client.apis.currencies.get_currencies()
        self.assertIn("data", response)
        self.assertTrue(len(response["data"]) > 0)
        print(response)

    def test_get_iata_codes(self):
        response = self.client.apis.iata_codes.get_iata_codes()
        self.assertIn("data", response)
        self.assertTrue(len(response["data"]) > 0)
        print(response)

    def test_get_rates(self):
        response = self.client.apis.search.get_rates()
        self.assertIn("data", response)
        self.assertTrue(len(response["data"]) > 0)
        print(response)

    def test_pre_book(self):
        response = self.client.apis.bookings.make_booking.pre_book(hotel_id="lp19e75", room_type_id="GMYS2MJQGYYTAML4KJDE47BSGAZDIMBYGMYDEMRVHF6DK7BXGE4DQNA")
        self.assertIn("data", response)
        self.assertTrue(len(response["data"]) > 0)
        print(response)

    def test_book(self):
        response = self.client.apis.bookings.make_booking.book(
            hotel_id="210011",
            guest_first_name="Steve",
            guest_last_name="Dupont",
            guest_email="dupont.s@hotmail.com",
            checkin="2024-07-20",
            checkout="2024-07-21"
        )
        self.assertIn("data", response)
        self.assertEqual(response["data"]["status"], "CONFIRMED")
        print(response)

    def test_list_bookings(self):
        response = self.client.apis.bookings.manage_booking.list_bookings()
        self.assertIn("data", response)
        self.assertTrue(len(response["data"]) > 0)
        print(response)

    def test_retrieve_booking(self):
        response = self.client.apis.bookings.manage_booking.retrieve_booking(booking_id="hSq2gVDrf")
        self.assertIn("data", response)
        self.assertEqual(response["data"]["bookingId"], "hSq2gVDrf")
        print(response)

    def test_cancel_booking(self):
        response = self.client.apis.bookings.manage_booking.cancel_booking(booking_id="hSq2gVDrf")
        self.assertIn("data", response)
        self.assertEqual(response["data"]["status"], "CANCELLED")
        print(response)

    # Tests for Vouchers
    def test_get_vouchers(self):
        response = self.client.apis.vouchers.get_vouchers()
        self.assertIn("data", response)
        self.assertTrue(len(response["data"]) > 0)
        print(response)

    def test_get_voucher_by_id(self):
        response = self.client.apis.vouchers.get_voucher_by_id(voucher_id="some_voucher_id")
        self.assertIn("data", response)
        self.assertEqual(response["data"]["id"], "some_voucher_id")
        print(response)

    # Tests for Loyalty Program
    def test_get_loyalty(self):
        response = self.client.apis.loyalty.get_loyalty()
        self.assertIn("data", response)
        self.assertTrue(len(response["data"]) > 0)
        print(response)

if __name__ == "__main__":
    unittest.main()
