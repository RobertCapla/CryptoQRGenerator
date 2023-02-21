import qrcode
import os


def create_qr_code(crypto_currency, crypto_address, amount=0, message='', filename="output"):
    """
    Create a QR code for a cryptocurrency address.

    Args:
        crypto_currency (str): The cryptocurrency symbol.
        crypto_address (str): The cryptocurrency address.
        amount (float, optional): The amount to be paid.
        message (str, optional): A message for the payment.
        filename (str, optional): The name of the file to save the QR code. Defaults to "output".

    Returns:
        str: The full path of the saved QR code image.
    """
    data = f"{crypto_currency}:{crypto_address}?amount={amount}&label=CryptoWallet.com&message={message}"
    try:
        # Create a QR code using the specified data
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the QR code image
        img_path = os.path.join(os.getcwd(), "qr_codes")
        os.makedirs(img_path, exist_ok=True)
        filename = f"{filename}.png"
        full_path = os.path.join(img_path, filename)
        img.save(full_path)
    except Exception as error:
        return error

    return full_path
