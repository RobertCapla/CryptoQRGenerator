import os
import qrcode

def create_qr_code(crypto_currency, crypto_address, amount, label, message):
    data = f"{crypto_currency}:{crypto_address}?amount={amount}&label{label}=&message={message}"
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
        img.save(os.path.join(img_path, f"output.png"))
    except Exception as error:
        return error
    return True
