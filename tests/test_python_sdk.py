import unittest
from unittest.mock import patch, MagicMock
from python_sdk.client import LiteApiClient

class TestPythonSDK(unittest.TestCase):

    def setUp(self):
        # Initialize the client with your API key
        self.client = LiteApiClient(api_key="your_api_key")  # Replace with your actual API key

    @patch('requests.request')
    def test_get_hotels(self, mock_request):
        # Mock response for get hotels
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "success", "data": [{"hotelId": "lp4c2bf"}]}
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        response = self.client.get("/data/hotels")
        print(response)  # Debugging: Print the response
        self.assertIn("data", response)
        self.assertTrue(len(response["data"]) > 0)

    @patch('requests.request')
    def test_get_hotel_details(self, mock_request):
        # Mock response for get hotel details
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "success", "data": {"id": "lp1897"}}  
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        response = self.client.get("/data/hotel", params={"hotelId": "lp1897"})
        print(response)  # Debugging: Print the response
        self.assertIn("data", response)
        self.assertTrue(len(response["data"]) > 0)

    @patch('requests.request')
    def test_get_voucher_by_id(self, mock_request):
        # Mock response for get voucher by ID
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "success", "data": {"id": "some_voucher_id"}}  
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        response = self.client.get("/vouchers/some_voucher_id")
        print(response)  # Debugging: Print the response
        self.assertIn("data", response)
        self.assertTrue(len(response["data"]) > 0)

    @patch('requests.request')
    def test_retrieve_booking(self, mock_request):
        # Mock response for retrieve booking
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "success", "data": {"bookingId": "hSq2gVDrf"}}  
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        response = self.client.get("/bookings/hSq2gVDrf")
        print(response)  # Debugging: Print the response
        self.assertIn("data", response)
        self.assertTrue(len(response["data"]) > 0)

    @patch('requests.request')
    def test_book(self, mock_request):
        # Mock response for booking
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "success", "data": {"status": "CONFIRMED"}}  
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        response = self.client.post("/bookings/book", data={
            "hotel_id": "210011",
            "guest_first_name": "Steve",
            "guest_last_name": "Dupont",
            "guest_email": "dupont.s@hotmail.com",
            "checkin": "2024-07-20",
            "checkout": "2024-07-21"
        })
        print(response)  # Debugging: Print the response
        self.assertIn("data", response)
        self.assertTrue(len(response["data"]) > 0)

    @patch('requests.request')
    def test_cancel_booking(self, mock_request):
        # Mock response for cancel booking
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "success", "data": {"status": "CANCELLED"}}  
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        response = self.client.post("/bookings/cancel", data={"booking_id": "hSq2gVDrf"})
        print(response)  # Debugging: Print the response
        self.assertIn("data", response)
        self.assertTrue(len(response["data"]) > 0)

    @patch('requests.request')
    def test_get_hotel_reviews(self, mock_request):
        # Mock response for get hotel reviews
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "success", "data": [{"review": "Great hotel!"}]}
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        response = self.client.get("/data/reviews", params={"hotelId": "lp4c2bf"})
        print(response)  # Debugging: Print the response
        self.assertIn("data", response)
        self.assertTrue(len(response["data"]) > 0)

    @patch('requests.request')
    def test_get_cities_by_country_code(self, mock_request):
        # Mock response for get cities by country code
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "success", "data": [{"city": "Dubai"}]}
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        response = self.client.get("/data/cities", params={"countryCode": "AE"})
        print(response)  # Debugging: Print the response
        self.assertIn("data", response)
        self.assertTrue(len(response["data"]) > 0)

    @patch('requests.request')
    def test_get_countries(self, mock_request):
        # Mock response for get countries
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "success", "data": [{"code": "AE", "name": "United Arab Emirates"}]}
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        response = self.client.get("/data/countries")
        print(response)  # Debugging: Print the response
        self.assertIn("data", response)
        self.assertTrue(len(response["data"]) > 0)

    @patch('requests.request')
    def test_get_currencies(self, mock_request):
        # Mock response for get currencies
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "success", "data": [{"code": "USD", "currency": "United States Dollar"}]}
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        response = self.client.get("/data/currencies")
        print(response)  # Debugging: Print the response
        self.assertIn("data", response)
        self.assertTrue(len(response["data"]) > 0)

    @patch('requests.request')
    def test_get_iata_codes(self, mock_request):
        # Mock response for get IATA codes
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "success", "data": [{"code": "JFK", "name": "John F Kennedy International"}]}
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        response = self.client.get("/data/iataCodes")
        print(response)  # Debugging: Print the response
        self.assertIn("data", response)
        self.assertTrue(len(response["data"]) > 0)

    @patch('requests.request')
    def test_get_rates(self, mock_request):
        # Mock response for get rates
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "success", "data": [{"hotelId": "lp4c2bf"}]}
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        response = self.client.post("/hotels/rates", data={})
        print(response)  # Debugging: Print the response
        self.assertIn("data", response)
        self.assertTrue(len(response["data"]) > 0)

    @patch('requests.request')
    def test_pre_book(self, mock_request):
        # Mock response for pre-booking
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "success", "data": {"prebookId": "abc123"}}
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        response = self.client.post("/bookings/prebook", data={"hotel_id": "lp19e75", "room_type_id": "GMYS2MJQGYYTAML4KJDE47BSGAZDIMBYGMYDEMRVHF6DK7BXGE4DQNA"})
        print(response)  # Debugging: Print the response
        self.assertIn("data", response)
        self.assertTrue(len(response["data"]) > 0)

    @patch('requests.request')
    def test_get_vouchers(self, mock_request):
        # Mock response for get vouchers
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "success", "data": [{"voucherCode": "DISCOUNT50"}]}
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        response = self.client.get("/vouchers")
        print(response)  # Debugging: Print the response
        self.assertIn("data", response)
        self.assertTrue(len(response["data"]) > 0)

    @patch('requests.request')
    def test_get_loyalty(self, mock_request):
        # Mock response for get loyalty program
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "success", "data": {"status": "active"}}
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        response = self.client.get("/loyalties")
        print(response)  # Debugging: Print the response
        self.assertIn("data", response)
        self.assertTrue(len(response["data"]) > 0)

if __name__ == "__main__":
    unittest.main()
