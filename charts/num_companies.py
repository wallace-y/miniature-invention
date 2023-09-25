import plotly.express as px
import pandas as pd


def read_data_from_csv(file_path):
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)

        # Convert the 'date' column to datetime
        df["date"] = pd.to_datetime(df["date"])

        return df
    except Exception as e:
        print(f"Error reading data from {file_path}: {str(e)}")
        return None


def create_bar_chart(data):
    if data is not None:
        y_columns = [col for col in data.columns if col != "date"]

        fig = px.bar(
            data,
            x="date",
            y=y_columns,
            labels={"date": "Date", "value": "Count"},
            title="Data Representation in Bar Chart",
        )
        fig.show()


# Usage:
file_path = (
    "./data/chart_data/num_companies_data.csv"  # Replace with the path to your CSV file
)
data = read_data_from_csv(file_path)

if data is not None:
    create_bar_chart(data)
