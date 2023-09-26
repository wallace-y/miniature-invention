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
        # Pivot the data to have company types as columns
        pivoted_data = data.melt(
            id_vars=["date"], var_name="company_type", value_name="count"
        )

        # Drop rows with missing values in the "count" column
        pivoted_data = pivoted_data.dropna(subset=["count"])

        fig = px.pie(
            pivoted_data,
            names="company_type",
            values="count",
            title="Pie Chart - Companies By Type",
        )
        return fig
