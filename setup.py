from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="crypto-qr-codes",
    version="0.1.8",
    author="Robert Capla",
    author_email="robert.capla@icloud.com",
    description="A package for generating QR codes for various cryptocurrencies",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RandoS-svk/CryptoQRGenerator",
    packages=["crypto_qr_codes"],
    install_requires=["qrcode"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
