import smartsheet
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

url = "https://api.smartsheet.com/2.0/sheets"

api_token2 = os.getenv("api_token2")

headers = {
    "Authorization": f"Bearer {api_token2}",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Sheets Retrieved successfully")
    sheets = response.json()

    with open("sheets.json", "w") as file:
        json.dump(sheets, file, indent=4)
else: 
    print(f"Error: {response.status_code}")
    print(response.json())