import unittest
from liteapi.sdk import LiteApi

class TestLiteApiReal(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up with a real API key and other necessary setup
        cls.api_key = "sand_c0155ab8-c683-4f26-8f94-b5e92c5797b9"
        cls.api = LiteApi(cls.api_key)

        cls.test_hotel_id = "lp1897"
        cls.test_offer_id = "GE5ESNBSIZKVMQ2QJJNEERSPKIZEMR2OIRKVOVCTKNFVMRCWKNLUWVKKGVDVMRKWGJEEWRSOIVEVCS2PJRFEUVKPK5JVKSKSI5LFKVKTLBFFMSSEJVJEGRCKIZHEMR2SGJBEYSSDIVJVIS2LJNHEIVJSK5FUSTCGI5LEKVKLJBFEKWSFJFITETSLJJFUKT2SKJLUSNKGKRDVKWSYJJHEYRKVK5BVUS22IZLESVKDKNFE4TCFJ5KVGRKHKJCFKVKRJNKUSRSJKRDU4Q2IJJDE4RKJKVFU4R2NGJCVOVSLGJEVUR2WJ5JEGVCLIJEVMU2WINIEUVSKIZGVEMSOJRDEWRJSKRFUGS2OIVCUGV2LIVEVMSCFK5LUWTKJJJGVKT2TGJFEYSSMKVHVGSSVJNJEMVKTK5JVKSJVINLE6VSDJZFFMSSGKVJDEV2HLJCEKS2VKNKEUNKJIZBVOU2FJFDEOVSFKZFUQSKWJZCUSUSLJ5GEUSSVJ5KEWWSJKJAVIT2RKNKUWQSKIVKVEQ2EJJLEMRSPKNBUOR22INCVGVCLINFTKRCVGJLUWRCJGVFVMR2VINDEUWSGIVFVIS2VJNFEGRKPKNFVUSKSINKTIUKTJ5ETKQ2WKVIVUU2KKZFEMUKSJNBEYSSDIVHVIMSTJNDEIVKDG5BFKR2NGJBTITS2KVIFCWSEIFGVEVKGKVMVIRKMJJJUONCRIRCU2WRSI5AVSRCVJVBFCUCSJJCTM7BWGI4TK7BSPRWHAMJYHE3XYMRNPRKVGRD4KVJXYMRQGI2C2MJSFUZTA7BSGAZDILJRGIWTGML4PQ3S4MBQ"
        cls.test_booking_id = "0QYXiyJGP"
        cls.test_voucher_id = "68"

    def test_get_countries(self):
        response = self.api.get_countries()
        self.assertEqual(response["status"], "success")
        self.assertIn("data", response)

    def test_get_cities_by_country_code(self):
        response = self.api.get_cities_by_country_code("US")
        self.assertEqual(response["status"], "success")
        self.assertIn("data", response)

    def test_get_currencies(self):
        response = self.api.get_currencies()
        self.assertEqual(response["status"], "success")
        self.assertIn("data", response)

    def test_get_hotels(self):
        response = self.api.get_hotels("US", "New York")
        self.assertEqual(response["status"], "success")
        self.assertIn("data", response)

    def test_get_hotel_details(self):
        response = self.api.get_hotel_details(self.test_hotel_id)
        self.assertEqual(response["status"], "success")
        self.assertIn("data", response)

    def test_get_hotel_reviews(self):
        response = self.api.get_hotel_reviews(self.test_hotel_id, limit=10)
        self.assertEqual(response["status"], "success")
        self.assertIn("data", response)

    def test_get_iata_codes(self):
        response = self.api.get_iata_codes()
        self.assertEqual(response["status"], "success")
        self.assertIn("data", response)

    def test_get_full_rates(self):
        response = self.api.get_full_rates({
            "checkin": "2024-12-01",
            "checkout": "2024-12-05",
            "hotelIds": [self.test_hotel_id],
            "occupancies": [{"adults": 2, "children": []}],
            "guestNationality": "US",
            "currency": "USD",
            "roomMapping": True
        })
        self.assertIn("data", response)

    def test_prebook(self):
        response = self.api.prebook({"offerId": self.test_offer_id})
        self.assertEqual(response["status"], "success")
        self.assertIn("data", response)

    def test_book(self):
        response = self.api.book({"offerId": self.test_offer_id})
        self.assertEqual(response["status"], "success")
        self.assertIn("data", response)

    def test_retrieve_booking(self):
        response = self.api.retrieve_booking(self.test_booking_id)
        self.assertEqual(response["status"], "success")
        self.assertIn("data", response)

    def test_cancel_booking(self):
        response = self.api.cancel_booking(self.test_booking_id)
        self.assertEqual(response["status"], "success")
        self.assertIn("data", response)

    def test_get_vouchers(self):
        response = self.api.get_vouchers()
        self.assertEqual(response["status"], "success")
        self.assertIn("data", response)

    def test_get_voucher_by_id(self):
        response = self.api.get_voucher_by_id(self.test_voucher_id)
        self.assertEqual(response["status"], "success")
        self.assertIn("data", response)

    def test_get_loyalty(self):
        response = self.api.get_loyalty()
        self.assertEqual(response["status"], "success")
        self.assertIn("data", response)

if __name__ == '__main__':
    unittest.main()
