import csv
import os
from collections import Counter
import re

# Directory containing the CSV files
csv_directory = "./data/formatted_data/"

# Output CSV file
output_csv_file = "./data/chart_data/company_name_analysis.csv"

# Create a Counter to store word frequency
company_name_words = Counter()

# Iterate through each CSV file in the directory
for filename in os.listdir(csv_directory):
    if filename.endswith(".csv"):
        file_path = os.path.join(csv_directory, filename)
        with open(file_path, "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                _, _, company_name = row
                # Split the company name into words based on spaces
                words = company_name.split()
                # Update the word frequency Counter
                company_name_words.update(words)

# Write the word frequency analysis to the output CSV file
with open(output_csv_file, "w", newline="") as csvfile:
    fieldnames = ["word", "frequency"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for word, frequency in company_name_words.items():
        writer.writerow({"word": word, "frequency": frequency})
