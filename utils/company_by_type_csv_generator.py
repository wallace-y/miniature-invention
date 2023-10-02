import csv
import os

# Directory containing the CSV files
csv_directory = "./data/formatted_data/"

# Output CSV file
output_csv_file = "./data/chart_data/num_companies_data.csv"

# Create an empty dictionary to store the data
combined_data = {}

# # Check if the output CSV file already exists
# if os.path.exists(output_csv_file):
#     # Read the existing data into the combined_data dictionary
#     with open(output_csv_file, "r") as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             date = row["date"]
#             combined_data[date] = row

# Iterate through each CSV file in the directory
for filename in os.listdir(csv_directory):
    if filename.endswith(".csv"):
        file_path = os.path.join(csv_directory, filename)
        with open(file_path, "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                date, type, _, _ = row  # ignore the 'name' col
                if date not in combined_data:
                    combined_data[date] = {"date": date}
                if type not in combined_data[date]:
                    combined_data[date][type] = 1
                else:
                    combined_data[date][type] = (
                        int(combined_data[date][type]) + 1
                    )  # Convert to int and increment

# Extract the unique types across all data
unique_types = set(
    type for data in combined_data.values() for type in data.keys() if type != "date"
)

# Write the combined data to the output CSV file
with open(output_csv_file, "w", newline="") as csvfile:
    fieldnames = ["date"] + list(unique_types)
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for data in combined_data.values():
        writer.writerow(data)
