import requests
from bs4 import BeautifulSoup
import os

url = "https://www.target.com/p/pok-233-mon-scarlet-violet-s10-5-elite-trainer-box-2-trading-cards/-/A-94636862#lnk=sametab"  # Replace with real URL
webhook_url = os.environ.get("DISCORD_WEBHOOK")  # Load from secret

headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    if "In Stock" in soup.text:
        message = {
            "content": f"✅ Product is **IN STOCK**!\n🔗 {url}"
        }
    else:
        message = {
            "content": f"❌ Product is still out of stock.\n🔗 {url}"
        }

    result = requests.post(webhook_url, json=message)
    if result.status_code != 204:
        print("Discord response:", result.text)

except Exception as e:
    error_message = {
        "content": f"⚠️ Error checking stock:\n```{str(e)}```"
    }
    requests.post(webhook_url, json=error_message)