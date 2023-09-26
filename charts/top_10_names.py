import csv
from collections import Counter

def get_top_names_from_csv(csv_file_path, exclude_words=[], top_n=5):
    name_frequencies = Counter()

    with open(csv_file_path, "r") as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # Skip the header row

        for row in csv_reader:
            word, frequency = row  # Extract the 'word' and 'frequency' columns
            word = word.strip()  # Remove leading/trailing spaces

            # Exclude specific words
            if word.upper() in [word.upper() for word in exclude_words]:
                continue

            # Update name frequencies based on the 'frequency' column
            name_frequencies[word] = int(frequency)

    # Get the top n names based on frequency
    top_names = name_frequencies.most_common(top_n)

    # Format the output strings with a space between name and amount
    formatted_top_names = [f"{name} {amount}" for name, amount in top_names]

    return formatted_top_names
