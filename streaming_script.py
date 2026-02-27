import requests
import json
import time
import random
from datetime import datetime

# 🔗 Replace with your Power BI Streaming Dataset Push URL
PUSH_URL = "PASTE_YOUR_PUSH_URL_HERE"

# Regions list
regions = ["North", "South", "East", "West"]

def generate_data():
    return [{
        "Timestamp": datetime.now().isoformat(),
        "Sales": random.randint(100, 500),
        "Region": random.choice(regions)
    }]

def send_data():
    try:
        data = generate_data()
        response = requests.post(
            PUSH_URL,
            data=json.dumps(data),
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            print("Data sent:", data)
        else:
            print("Failed:", response.text)

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    print("Streaming started... Press CTRL+C to stop")
    while True:
        send_data()
        time.sleep(3)  # sends data every 3 seconds
