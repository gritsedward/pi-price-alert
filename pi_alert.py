import requests
import os

BOT_TOKEN = os.environ["8998290195:AAF9TXLeBKZdHG6qqHvwItYCeGBlbds45LM"]
CHAT_ID = os.environ["561404614"]

TARGET_PRICE = 1.00

url = "https://api.coingecko.com/api/v3/simple/price?ids=pi-network&vs_currencies=usd"

response = requests.get(url)

price = response.json()["pi-network"]["usd"]

print(f"Current PI price: {price}")

if price >= TARGET_PRICE:
    message = f"🚀 PI price alert!\n\nCurrent price: ${price}"

    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(
        telegram_url,
        data={
            "chat_id": CHAT_ID,
            "text": message
        }
    )

    print("Alert sent")
else:
    print("Price below target")
