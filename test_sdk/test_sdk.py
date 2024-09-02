import sys
import os

# Add the parent directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from python_sdk.client import LiteApiClient

API_KEY = "sand_e7be24f5-f004-484c-9103-f4eba210b58f"

def test_get_hotels():
    try:
        client = LiteApiClient(api_key=API_KEY)
        response = client.get("/data/hotels", params={"countryCode": "IT"})
        print("Response from get hotels:", response)
        assert "data" in response
        assert len(response["data"]) > 0
    except Exception as e:
        print("An error occurred during test_get_hotels:", e)
        raise

def test_get_hotel_details():
    try:
        client = LiteApiClient(api_key=API_KEY)
        response = client.get("/data/hotel", params={"hotelId": "lp1897"})
        print("Response from get hotel details:", response)
        assert "data" in response
        assert len(response["data"]) > 0
    except Exception as e:
        print("An error occurred during test_get_hotel_details:", e)
        raise

def test_get_hotel_reviews():
    try:
        client = LiteApiClient(api_key=API_KEY)
        response = client.get("/data/reviews", params={"hotelId": "lp4c2bf"})
        print("Response from get hotel reviews:", response)
        assert "data" in response
        assert len(response["data"]) > 0
    except Exception as e:
        print("An error occurred during test_get_hotel_reviews:", e)
        raise

def test_get_cities_by_country_code():
    try:
        client = LiteApiClient(api_key=API_KEY)
        response = client.get("/data/cities", params={"countryCode": "IT"})
        print("Response from get cities by country code:", response)
        assert "data" in response
        assert len(response["data"]) > 0
    except Exception as e:
        print("An error occurred during test_get_cities_by_country_code:", e)
        raise

def test_get_countries():
    try:
        client = LiteApiClient(api_key=API_KEY)
        response = client.get("/data/countries")
        print("Response from get countries:", response)
        assert "data" in response
        assert len(response["data"]) > 0
    except Exception as e:
        print("An error occurred during test_get_countries:", e)
        raise

def test_get_currencies():
    try:
        client = LiteApiClient(api_key=API_KEY)
        response = client.get("/data/currencies")
        print("Response from get currencies:", response)
        assert "data" in response
        assert len(response["data"]) > 0
    except Exception as e:
        print("An error occurred during test_get_currencies:", e)
        raise

def test_get_iata_codes():
    try:
        client = LiteApiClient(api_key=API_KEY)
        response = client.get("/data/iataCodes")
        print("Response from get IATA codes:", response)
        assert "data" in response
        assert len(response["data"]) > 0
    except Exception as e:
        print("An error occurred during test_get_iata_codes:", e)
        raise

def test_get_rates():
    try:
        client = LiteApiClient(api_key=API_KEY)
        response = client.post("/hotels/rates", data={
            "hotelIds": ["lp1897"],  
            "checkin": "2024-12-30",
            "checkout": "2024-12-31",
            "currency": "USD",
            "guestNationality": "US",
            "occupancies": [{"adults": 2, "children": []}]
        })
        print("Response from get rates:", response)
        assert "data" in response
        assert len(response["data"]) > 0
    except Exception as e:
        print("An error occurred during test_get_rates:", e)
        raise

def test_pre_book():
    try:
        client = LiteApiClient(api_key=API_KEY)
        
        payload = {
            "usePaymentSdk": True,  # Ensure this is a boolean
            "offerId": "GE5ESNKHKZJVMQ2GJJLEERSPKRFUUR2OINDEOVCTKVEVURCWKNGTEVKJKZDVKRKWGJEEURK2KVEVGMSPJNFEWVKPKNFVUSKSJBKTEV2TLFETKS2UI5JEGVCKLJHEMS2SGJNEOSSNIZJVIS2LJFJEIVKTK5FUKSKWJBCUKVKTJBFEMTSGJFIUUWCJJJFFKT2RJMZESUSFKUZFGU2UJE2UOVSTK5BVUTCKI5CTMVCCKZFE4TCFJ5HDERCLLJDFKNCOKNDUUTSLKRCVES2RJNDE4RKLKEZE4SKOINDECVKLGJEVEQ2VGZIVGVKLIJFEKV2WINDEWWSKKZJVIMSLI5NEGRKHKRJTES2OIRLEWV2TIVEVMSCVKVLUWSCLIUZEKSKRJNHEWSSNIU3FMU2EJRBEIVSHKVJUKSJVJVLFKUSDKRFFURSFJFJDETSMIZFUMR2UINFUWNKEKVJU4Q2VJJGTGVKHKUZEUTCKIVCVCV2LJZFUUSKVJ5JUUU2JKJBFKMSVKNKEUQSDKZJVMQ2MJJLEERSDKVBVER2KINCUGTRSIRFU4RCVJNLUWVKKGVDVKSKOINEEURK2IVEVCS2OJRFEWVKPKFFVGS22INLESV2TIVFE4RSFJFJEUVKKIZHEMR2SGJBEYSSDIVJVIQ2LJNFEIVKTKYZFKSKWJBKVKUKLJBEVKWSGJFLEWTSJJJEVQWKNKJLUOWJTKM2E4WSYKBIVURCBJVJFKRSVLFKEKTCKKNEEKUKEINHEUMSHIFMUIVKNIJIVAUSKIU3HYNRSHE2XYMT4NRYDCOBZG56DELL4KVJUI7CVKN6DEMBSGQWTCMRNGMYHYMRQGI2C2MJSFUZTC7D4GEYS4MBQ"
        }
        
        # Make the POST request using the booking service
        response = client.post("/rates/prebook", data=payload, use_service="booking")
        
        print("Response from prebook:", response)
        assert "data" in response
        assert len(response["data"]) > 0, "Response data is empty"
    except Exception as e:
        print("An error occurred during test_pre_book:", e)
        raise


def test_book_hotel():
    try:
        client = LiteApiClient(api_key=API_KEY)
        
        payload = {
            "holder": {
                "firstName": "Steve",
                "lastName": "Doe",
                "email": "s.doe@liteapi.travel"
            },
            "payment": { "method": "ACC_CREDIT_CARD" },
            "prebookId": "qkXV4GYJu",  # Ensure this is a valid prebook ID obtained from prebooking
            "guests": [
                {
                    "occupancyNumber": 1,
                    "remarks": "quiet room please",
                    "firstName": "Sunny",
                    "lastName": "Mars",
                    "email": "s.mars@liteapi.travel"
                }
            ]
        }
        
        response = client.post("/rates/book", data=payload, use_service="booking")
        
        print("Response from book hotel:", response)
        assert "data" in response
        assert len(response["data"]) > 0  
    except Exception as e:
        print("An error occurred during test_book_hotel:", e)
        raise

def test_retrieve_booking():
    try:
        client = LiteApiClient(api_key=API_KEY)

        booking_id = "twopYuLE_"
        endpoint = f"/bookings/{booking_id}"

        response = client.get(endpoint, use_service="booking")

        print("Response from retrieve booking:", response)
        assert "data" in response
        assert len(response["data"]) > 0  
    except Exception as e:
        print("An error occurred during test_retrieve_booking:", e)
        raise

def test_cancel_booking():
    try:
        client = LiteApiClient(api_key=API_KEY)

        booking_id = "hEL4KtchC"  # Replace with the actual booking ID you want to cancel
        endpoint = f"/bookings/{booking_id}"

        response = client.put(endpoint, headers={
            "accept": "application/json",
            "X-API-Key": API_KEY
        }, use_service="booking")

        print("Response from cancel booking:", response)
        assert "data" in response
        assert len(response["data"]) > 0  # 
    except Exception as e:
        print("An error occurred during test_cancel_booking:", e)
        raise

def test_get_vouchers():
    try:
        client = LiteApiClient(api_key=API_KEY)
        response = client.get("/vouchers", use_service="voucher")
        print("Response from get vouchers:", response)
        assert "data" in response
        assert len(response["data"]) > 0
    except Exception as e:
        print("An error occurred during test_get_vouchers:", e)
        raise

def test_get_voucher_by_id():
    try:
        client = LiteApiClient(api_key=API_KEY)
        
        voucher_id = "68"  # Replace with the actual voucher ID you want to retrieve
        endpoint = f"/vouchers/{voucher_id}"

        response = client.get(endpoint, use_service="voucher")

        print(f"Response from get voucher by ID {voucher_id}:", response)
        assert "data" in response
        assert len(response["data"]) > 0  
    except Exception as e:
        print("An error occurred during test_get_voucher_by_id:", e)
        raise

def test_get_loyalty():
    try:
        client = LiteApiClient(api_key=API_KEY)
        response = client.get("/loyalties")
        print("Response from get loyalty program details:", response)
        assert "data" in response
        assert len(response["data"]) > 0
    except Exception as e:
        print("An error occurred during test_get_loyalty:", e)
        raise

if __name__ == "__main__":
    try:
        test_get_hotels()
        test_get_hotel_details()
        test_get_hotel_reviews()
        test_get_cities_by_country_code()
        test_get_countries()
        test_get_currencies()
        test_get_iata_codes()
        test_get_rates()
        test_pre_book()
        test_book_hotel()
        test_retrieve_booking()
        test_cancel_booking()  
        test_get_vouchers()
        test_get_voucher_by_id()
        test_get_loyalty()
    except Exception as e:
        print("An error occurred during testing:", e)
