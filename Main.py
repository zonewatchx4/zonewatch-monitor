import os
import time
import requests

# Load secrets from Railway Variables
FB_PAGE_TOKEN = os.getenv("FB_PAGE_TOKEN")
X_BEARER_TOKEN = os.getenv("X_BEARER_TOKEN")

def monitor_facebook():
    url = f"https://graph.facebook.com/v18.0/me?access_token={FB_PAGE_TOKEN}"
    try:
        response = requests.get(url)
        print("Facebook response:", response.json())
    except Exception as e:
        print("Facebook error:", e)

def monitor_x():
    url = "https://api.x.com/2/tweets/search/recent?query=ClayHiggins"
    headers = {"Authorization": f"Bearer {X_BEARER_TOKEN}"}
    try:
        response = requests.get(url, headers=headers)
        print("X response:", response.json())
    except Exception as e:
        print("X error:", e)

def main():
    print("🚀 ZoneWatch Monitor started")
    while True:
        monitor_facebook()
        monitor_x()
        print("Cycle complete. Sleeping 60s...\n")
        time.sleep(60)  # check every minute

if __name__ == "__main__":
    main()
