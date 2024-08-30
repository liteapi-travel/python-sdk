import requests
from datetime import datetime, timedelta
import json
import sentry_sdk
from python_sdk.client import LiteApiClient

# Initialize Sentry for error tracking
sentry_sdk.init(
    dsn="https://fa8a8f6fefc231a3bf78da6d8914d9f3@o4507232451952640.ingest.us.sentry.io/4507570819760128",
    traces_sample_rate=1.0
)

API_KEY = "sand_ca230deb-5a6b-42e7-bb72-869facd8892b"
BETTERUPTIME_URL = "your_betteruptime_url_here"  # Replace with actual BetterUptime URL

# Initialize LiteApiClient
client = LiteApiClient(api_key=API_KEY)

def signal_betteruptime():
    """ Signal BetterUptime with a success status """
    try:
        response = requests.post(
            BETTERUPTIME_URL,
            headers={"Content-Type": "application/json"},
            json={"status": "success"}
        )
        response.raise_for_status()
        print("Signaled BetterUptime successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Error signaling BetterUptime: {e}")
        sentry_sdk.capture_exception(e)

def fetch_json(endpoint, method='GET', data=None):
    """ Helper function to fetch JSON data using LiteApiClient """
    try:
        if method == 'GET':
            response = client.get(endpoint)
        elif method == 'POST':
            response = client.post(endpoint, data=data)
        else:
            raise ValueError("Invalid method. Use 'GET' or 'POST'.")
        
        if response['status'] != 'success':
            raise Exception(response['error'])

        return response['data']

    except Exception as e:
        print(f"Error fetching data from {endpoint}: {e}")
        sentry_sdk.capture_exception(e)
        raise

def health_check():
    """ Main health check function """
    try:
        # 1. Fetch a list of hotels in Verona, Italy
        hotels = fetch_json("/data/hotels", method='GET', data={"cityName": "Verona", "countryCode": "IT", "limit": 200})

        if not hotels:
            raise Exception("No hotels found")

        print(f"Found {len(hotels)} hotels.")

        # 2. Fetch rates for the found hotels
        checkin_date = (datetime.now() + timedelta(days=180)).strftime('%Y-%m-%d')
        checkout_date = (datetime.now() + timedelta(days=181)).strftime('%Y-%m-%d')
        rates_data = {
            "hotelIds": [hotel['id'] for hotel in hotels],
            "checkin": checkin_date,
            "checkout": checkout_date,
            "occupancies": [{"adults": 2}],
            "currency": "USD",
            "guestNationality": "US",
            "timeout": 10
        }

        rates_response = fetch_json("/hotels/rates", method='POST', data=rates_data)

        if not rates_response:
            raise Exception("No rates found")

        print(f"Found rates for {len(rates_response)} hotels.")

        offer_id = rates_response[0]['roomTypes'][0]['offerId']
        print(f"Found offer: {offer_id}")

        # 3. Make a pre-booking request
        prebook_data = {
            "offerId": offer_id,
            "usePaymentSdk": False
        }
        prebook_response = fetch_json("/rates/prebook", method='POST', data=prebook_data)

        prebook_id = prebook_response['prebookId']
        print(f"Prebooked with prebookId: {prebook_id}")

        # 4. Make a booking request
        booking_data = {
            "holder": {
                "firstName": "Uptime",
                "lastName": "Monitor",
                "email": "monitor@liteapi.travel"
            },
            "payment": {
                "method": "ACC_CREDIT_CARD"
            },
            "prebookId": prebook_id,
            "guests": [{
                "occupancyNumber": 1,
                "remarks": "quiet room please",
                "firstName": "Uptime",
                "lastName": "Monitor",
                "email": "monitor@liteapi.travel"
            }]
        }

        booking_response = fetch_json("/rates/book", method='POST', data=booking_data)

        if booking_response['status'] != 'CONFIRMED':
            raise Exception("Booking failed")

        print(f"Booking confirmed with status: {booking_response['status']}")

        # 5. Signal BetterUptime if all steps are successful
        signal_betteruptime()

    except Exception as e:
        print(f"Health check failed: {e}")
        sentry_sdk.capture_exception(e)

if __name__ == "__main__":
    health_check()
