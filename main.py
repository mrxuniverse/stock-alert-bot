import requests
from bs4 import BeautifulSoup
import os

url = "https://www.target.com/p/pok-233-mon-scarlet-violet-s10-5-elite-trainer-box-2-trading-cards/-/A-94636862#lnk=sametab"
webhook_url = os.environ.get("DISCORD_WEBHOOK")

headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    # Example: check if product is in stock
    if "Out of stock" in soup.text:
        message = {"content": "❌ Product still out of stock."}
    else:
        message = {"content": "✅ Product is in stock!"}

    requests.post(webhook_url, json=message)

except Exception as e:
    error_message = {"content": f"⚠ Error: {str(e)}"}
    requests.post(webhook_url, json=error_message)