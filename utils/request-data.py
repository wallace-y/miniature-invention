import requests
import json
import os
import sys

from dotenv import load_dotenv

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

# Now you can import modules from the 'utils' package
import format_data

# Load the stored environment variables
load_dotenv()

dates = [
    "2023-09-09",
    "2023-09-10",
    "2023-09-11",
    "2023-09-12",
    "2023-09-13",
    "2023-09-14",
    "2023-09-15",
    "2023-09-16",
    "2023-09-17",
]

api_key = os.getenv("API_KEY")


for date in dates:
    url = f"https://api.company-information.service.gov.uk/advanced-search/companies?incorporated_from={date}&incorporated_to={date}&size=5000"
    headers = {"Authorization": f"{api_key}"}

    def call_CH_api():
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Failed to fetch data for date {date}: {response.reason}")
        else:
            data = response.json()
            if data:
                json_file = f"./data/{date[:7]}/{date}-data.json"
                with open(json_file, "w") as json_file:
                    json.dump(data, json_file, indent=4)
            json_file.close()
            print(f"Data for date {date} saved successfully.")
        format_data.save_json_api_data_to_csv(f"./data/{date[:7]}/{date}-data.json")

    call_CH_api()
