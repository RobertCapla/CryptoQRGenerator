from setuptools import setup, find_packages

setup(
    name='crypto-qr-codes',
    version='0.1.0',
    description='Python package for generating QR codes for crypto payments',
    author='Robert Capla',
    author_email='robert.capla@icloud.com',
    packages=find_packages(),
    install_requires=[
        'qrcode',
    ],
)
