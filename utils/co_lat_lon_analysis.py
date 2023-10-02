import csv
import os
import re
import requests  # Import the requests library for making API requests

# Directory containing the CSV files
csv_directory = "./data/formatted_data/"

# Output CSV file
output_csv_file = "./data/chart_data/lat_long_data.csv"


def read_csv_and_get_lat_lng(input_file, output_file, max_instances=250):
    # Initialize a CSV writer for the output file
    with open(output_file, "w", newline="") as csvfile:
        fieldnames = ["name", "latitude", "longitude"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Read data from the input CSV file
        with open(input_file, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            instance_count = 0
            for row in reader:
                if instance_count >= max_instances:
                    break

                postcode = row["postcode"]

                # Request latitude and longitude data from Postcode.io
                response = requests.get(
                    f"https://api.postcodes.io/postcodes/{postcode}"
                )
                data = response.json()

                if response.status_code == 200 and "result" in data:
                    latitude = data["result"]["latitude"]
                    longitude = data["result"]["longitude"]
                else:
                    # Handle cases where postcode data is not available
                    latitude = "N/A"
                    longitude = "N/A"

                # Write data to the output CSV file
                writer.writerow(
                    {
                        "name": row["name"],
                        "latitude": latitude,
                        "longitude": longitude,
                    }
                )

                instance_count += 1


# Iterate through CSV files in the directory
for filename in os.listdir(csv_directory):
    if filename.endswith(".csv"):
        input_file = os.path.join(csv_directory, filename)
        read_csv_and_get_lat_lng(input_file, output_csv_file)
