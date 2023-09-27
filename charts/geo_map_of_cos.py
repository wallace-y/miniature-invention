import plotly.express as px
import pandas as pd


def read_data_from_csv(file_path):
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)

        print("here at least")
        return df
    except Exception as e:
        print(f"Error reading data from {file_path}: {str(e)}")
        return None


def create_scattermap(data):
    if data is not None:
        uk_bounds = {"lon": [-10, 2], "lat": [49, 61]}

        fig = px.density_mapbox(
            data,
            lat="latitude",  # Replace with the actual column name for latitude
            lon="longitude",  # Replace with the actual column name for longitude
            hover_name="name",  # Replace with the actual column name for company name
            title="Cluster Map - Company Locations",
            center={
                "lat": 54.7024,
                "lon": -3.2766,
            },  # Centered on a point within the UK
            zoom=3.5,  # Adjust the zoom level as needed
            mapbox_style="open-street-map",  # Specify the map style
            opacity=0.7,  # Adjust the opacity of the clusters
            radius=5,  # Adjust the cluster radius
        )

        fig.update_geos(
            fitbounds="locations",
            lataxis_range=uk_bounds["lat"],
            lonaxis_range=uk_bounds["lon"],
        )

        return fig
