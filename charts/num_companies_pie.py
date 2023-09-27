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


def create_pie_chart(data):
    if data is not None:
        y_columns = [col for col in data.columns if col != "date"]

        all_columns = ["date"] + y_columns
        data["total"] = data[y_columns].sum(axis=1)

        fig = px.pie(
            data,
            names="date",
            values="total",
            title="Pie Chart - Companies By Day Of Incorporation",
        )

        fig.update_layout(font_color="#333")
        return fig
