import qrcode
import os


def create_qr_code(crypto_currency, crypto_address, amount=None, label=None, message=None, filename="output.png"):
    data = f"{crypto_currency}:{crypto_address}"
    if amount is not None:
        data += f"?amount={amount}"
    if label is not None:
        data += f"&label={label}"
    if message is not None:
        data += f"&message={message}"
    try:
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img_path = os.path.join(os.getcwd(), "qr_codes")
        os.makedirs(img_path, exist_ok=True)
        full_path = os.path.join(img_path, filename)
        img.save(full_path)
    except Exception as error:
        return error
    return full_path
