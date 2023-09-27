# Company Incorporation Analysis App

The hosted application should be accessible at [https://companie-house-incorporation-stats.onrender.com](https://companie-house-incorporation-stats.onrender.com).

## Overview

The Company Incorporation Analysis App is a Python-based web application designed to provide insights and visualizations on UK companies' incorporation data. It utilizes the Dash framework for creating interactive and informative dashboards to help users better understand the trends and statistics related to company formations during this timeframe.

## Getting Started

To get started with the Company Incorporation Analysis App, follow these steps:

1. Clone the repository to your local machine:

```
git clone https://github.com/yourusername/company-incorporation-analysis.git

```

2. Install the required dependencies by running:

```
pip install -r requirements.txt

```

3. Navigate to the app directory:

```
cd company-incorporation-analysis

```

4. Run the application:

```
python app.py

```

The app should be accessible at [http://localhost:8050/](http://localhost:8050/).

## Features

The Company Incorporation Analysis App provides the following features:

1. **Bar Chart - Number of Companies By Type**: Visualizes the number of companies incorporated in the past week.

2. **Pie Chart - Number of Companies by Type**: Displays a pie chart representing the distribution of company types.

3. **Top 10 Words**: Lists the top 10 words found in company names, excluding common words like "LTD," "LIMITED," and others.

4. **Line Chart - Number of Companies Past Month**: Shows a line chart depicting the trend in company incorporations over the past month.

## Usage

Upon running the application, you can access the various features and charts via the web interface. Here's a brief overview of how to use each feature:

- **Bar Chart - Number of Companies Past Week**: This chart displays the number of companies incorporated in the past week. Hover over the bars to view specific counts for each date.

- **Pie Chart - Number of Companies by Type**: This pie chart visualizes the distribution of company types. Hover over the sections to see the percentage and count for each type.

- **Top 10 Words**: This section lists the top 10 words found in company names during the specified period. These words are ranked by frequency, and common words like "LTD" and "LIMITED" are excluded.

- **Line Chart - Number of Companies Past Month**: This line chart illustrates the trend in company incorporations over the past month. You can hover over the data points to view specific counts for each date.

## Data Sources

The Company Incorporation Analysis App uses CSV data files located in the `./data/chart_data/` directory:

- `num_companies_data.csv`: Contains data for the bar chart displaying the number of companies in the past week.
- `company_name_analysis.csv`: Contains data for the analysis of company names, used to generate the "Top 10 Words" list.

You can replace these files with your own data if needed.

## Dependencies

The application relies on the following Python libraries and components:

- `pandas`: Used for data manipulation and analysis.
- `dash`: The core framework for building web applications.
- `dash-core-components` and `dash-html-components`: Libraries for creating Dash components.
- Other libraries listed in the `requirements.txt` file.
