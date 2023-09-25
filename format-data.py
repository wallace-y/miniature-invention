import json
import csv

file_name = "data/2023-09/2023-09-24-data.json"


def read_json_api_data(file_name):
    with open(file_name, "r") as json_file:
        data = json.load(json_file)
        return data["items"]


def save_json_api_data_to_csv():
    company_data = read_json_api_data(file_name)

    with open(
        f"./data/formatted_data/{company_data[0]['date_of_creation']}.csv",
        "w",
        newline="",
    ) as csvfile:
        fieldnames = ["date", "type"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in company_data:
            writer.writerow(
                {
                    "date": item["date_of_creation"],
                    "type": item["company_type"],
                }
            )


save_json_api_data_to_csv()
