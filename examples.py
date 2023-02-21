from crypto_qr_codes.qr import create_qr_code

# Generate QR code for Bitcoin with an amount of 2 BTC
create_qr_code(crypto_currency="bitcoin", 
               crypto_address="18Qz324MxCwBbrWqNv1Ew3vcgpi9N9DmXM", 
               filename="bitcoin", 
               amount=2)

# Generate QR code for Ethereum with an amount of 10 ETH
create_qr_code(crypto_currency="ethereum", 
               crypto_address="0xb794f5ea0ba39494ce839613fffba74279579268", 
               filename="ethereum", 
               amount=10)

# Generate QR code for Litecoin with an amount of 5 LTC
create_qr_code(crypto_currency="litecoin", 
               crypto_address="LQGkxvJNjkYZDZfTZjUE8ARsWYNJwtaqaY", 
               filename="litecoin", 
               amount=5)

# Generate QR code for Dogecoin with an amount of 100 DOGE
create_qr_code(crypto_currency="dogecoin", 
               crypto_address="DKCSXC7noe6aCJ6SjxBqy3kyEYpU4Xnt4a", 
               filename="dogecoin", 
               amount=100)

# Generate QR code for Ripple with an amount of 50 XRP
create_qr_code(crypto_currency="ripple", 
               crypto_address="rEb8TK3gBgk5auZkwc6sHnwrGVJH8DuaLh", 
               filename="ripple", 
               amount=50)

# Generate QR code for Cardano with an amount of 25 ADA
create_qr_code(crypto_currency="cardano", 
               crypto_address="addr1qx8s6df33y6wddqr6txhx22m4a0cq2c0qxzqck3prgj7zrlfw6g2qag3wqaxhxykuzdlh07gcj5fzrr5ysudfq5dse8r0nkkkr", 
               filename="cardano", 
               amount=25)

# Generate QR code for Polkadot with an amount of 20 DOT
create_qr_code(crypto_currency="polkadot", 
               crypto_address="14N9NozDZM2g1h8LZoyQy1wZZdb3eJyv8TEWg5FZ9mUGJRGE", 
               filename="polkadot", 
               amount=20)

# Generate QR code for Binance Coin with an amount of 15 BNB
create_qr_code(crypto_currency="binancecoin", 
               crypto_address="bnb1v8tnjepyp9zhtkfvn9qnsp7asfj6s5d5k5n5r5", 
               filename="binancecoin", 
               amount=15)

# Generate QR code for Chainlink with an amount of 12 LINK
create_qr_code(crypto_currency="chainlink", 
               crypto_address="0x32dbd1c5e30c0d5a669f51bc19f1b43347dcb2a9", 
               filename="chainlink", 
               amount=12)

