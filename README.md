# Crypto QR Codes

Crypto QR Codes is a Python package that allows you to generate QR codes for various cryptocurrencies.

## Installation

You can install Crypto QR Codes using pip:

```bash
pip install crypto-qr-codes
```
## Usage

To use Crypto QR Codes, import the `create_qr_code` function from the `crypto_qr_codes.qr` module. Here's an example:

```python
from crypto_qr_codes.qr import create_qr_code

crypto_currency = "bitcoin"
crypto_address = "18Qz324MxCwBbrWqNv1Ew3vcgpi9N9DmXM"
amount = 0.1
message = "Payment for goods"

create_qr_code(crypto_currency, crypto_address, amount, message)
```
## Parameters
The create_qr_code function takes the following parameters:

crypto_currency (required): A string that represents the cryptocurrency. <br>
crypto_address (required): A string that represents the cryptocurrency address. <br>
amount (optional): A float that represents the amount to be paid.<br>
message (optional): A string that represents a message for the payment.<br>
filename (optional): A string that represents the name of the file to save the QR code. Defaults to output.png.
## Returns
The create_qr_code function returns the full path of the generated QR code image file.
## Testing
To run the tests for Crypto QR Codes, run the following command:
```bash
python -m unittest tests.test_qr
```
## Examples
You can check the `examples.py` file for examples of how to use the package. The outputs of the examples are stored in the `qr_codes` folder.
## License
This project is licensed under the MIT License.




