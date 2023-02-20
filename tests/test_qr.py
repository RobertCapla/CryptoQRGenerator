import os
import unittest
from crypto_qr_codes.qr import create_qr_code

class TestQR(unittest.TestCase):
    def test_create_qr_code(self):
        crypto_currency = "BTC"
        crypto_address = "1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2"
        amount = "0.001"
        label = "Swapleo.com"
        message = "Payment"
        result = create_qr_code(crypto_currency, crypto_address, amount, label, message)
        self.assertTrue(result)
        img_path = os.path.join(os.getcwd(), "qr_codes", "output.png")
        self.assertTrue(os.path.isfile(img_path))

if __name__ == '__main__':
    unittest.main()
