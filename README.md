# Crypto QR Codes

Crypto QR Codes is a Python package that allows you to generate QR codes for various cryptocurrencies.

## Installation

You can install Crypto QR Codes using pip:

pip install crypto-qr-codes


## Usage

To use Crypto QR Codes, import the `create_qr_code` function from the `crypto_qr_codes.qr` module. Here's an example:

```python
from crypto_qr_codes.qr import create_qr_code

crypto_currency = "BTC"
crypto_address = "3N8auHJMn6GQzVjKXF5e2eNn5b6d4wy4G4"
amount = 0.1
label = "My Bitcoin Address"
message = "Payment for goods"

create_qr_code(crypto_currency, crypto_address, amount, label, message)
