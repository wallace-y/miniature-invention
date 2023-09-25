import requests
import json
import os
from dotenv import load_dotenv

# Load the stored environment variables
load_dotenv()

api_key = os.getenv("API_KEY")
date = "2023-09-24"
url = f"https://api.company-information.service.gov.uk/advanced-search/companies?incorporated_from={date}&incorporated_to={date}&size=50"
headers = {"Authorization": f"{api_key}"}


def call_CH_api():
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(response.reason)
    else:
        data = response.json()
        if data:
            json_file = f"./data/{date[:7]}/{date}-data.json"
            with open(json_file, "w") as json_file:
                json.dump(data, json_file, indent=4)
            print("Done")


call_CH_api()
