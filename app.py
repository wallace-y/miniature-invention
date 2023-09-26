import pandas as pd
from dash import Dash, dcc, html
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, "..")  # Go up one level
sys.path.append(parent_dir)

from charts import (
    num_co_bar_past_week,
    num_companies_pie,
    num_cos_pie_by_type,
    num_co_line_past_month,
)

# Load your data here
file_path = (
    "./data/chart_data/num_companies_data.csv"  # Replace with the path to your CSV file
)
num_companies_data = num_co_bar_past_week.read_data_from_csv(file_path)
num_companies_pie_data = num_companies_pie.read_data_from_csv(file_path)
num_companies_pie_data_type = num_cos_pie_by_type.read_data_from_csv(file_path)
num_co_line_past_month_data = num_co_line_past_month.read_data_from_csv(file_path)


app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="Company Incorporation Analysis", className="header-title"),
        html.P(
            children=(
                "Analysis of UK companies incorporation data in the past week 18-09-2023 - 24-09-2023"
            ),
        ),
        dcc.Graph(
            figure=num_co_bar_past_week.create_bar_chart(num_companies_data),
            className="dash-graph",
        ),
        dcc.Graph(
            figure=num_companies_pie.create_pie_chart(num_companies_pie_data),
            className="dash-graph",
        ),
        dcc.Graph(
            figure=num_cos_pie_by_type.create_pie_chart(num_companies_pie_data_type),
            className="dash-graph",
        ),
        dcc.Graph(
            figure=num_co_line_past_month.create_line_chart(
                num_co_line_past_month_data
            ),
            className="dash-graph",
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
