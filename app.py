import pandas as pd
from dash import Dash, dcc, html
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, "..")  # Go up one level
sys.path.append(parent_dir)

from charts import num_companies, num_companies_pie

# Load your data here
file_path = (
    "./data/chart_data/num_companies_data.csv"  # Replace with the path to your CSV file
)
num_companies_data = num_companies.read_data_from_csv(file_path)
num_companies_pie_data = num_companies_pie.read_data_from_csv(file_path)


app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="Company Analytics"),
        html.P(
            children=("Analyze the incorporation of UK companies in the past week"),
        ),
        dcc.Graph(figure=num_companies.create_bar_chart(num_companies_data)),
        dcc.Graph(figure=num_companies_pie.create_pie_chart(num_companies_pie_data)),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
