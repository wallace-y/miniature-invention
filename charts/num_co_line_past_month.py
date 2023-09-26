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


def create_line_chart(data):
    if data is not None:
        y_columns = [col for col in data.columns if col != "date"]

        all_columns = ["date"] + y_columns
        data["total"] = data[y_columns].sum(axis=1)

        data = data.sort_values(by="date")

        fig = px.line(
            data,
            x="date",
            y="total",
            labels={"date": "Date", "total": "Count"},
            title="Companies Incorporated By Type By Day Past Month",
        )
        return fig
