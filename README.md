# NYC Taxi Data Analysis

This project analyzes New York City yellow taxi trip data and visualizes hourly demand patterns.

## Description

The script processes taxi trip data from a Parquet file, extracts temporal features, and generates a visualization showing the distribution of taxi trips across different hours of the day.

## Requirements

- Python 3.x
- pandas
- matplotlib

## Installation

Install the required packages using pip:

```
pip install pandas matplotlib pyarrow
```

Note: pyarrow is required for reading Parquet files.

## Usage

1. Place your taxi data file (yellow_tripdata_2019-08.parquet) in the same directory as the script.

2. Run the script:

```
python data.py
```

3. The script will:
   - Load and display basic statistics of the dataset
   - Extract hour and date information from pickup timestamps
   - Calculate trip counts by hour
   - Generate and save a plot as figure_hourly_demand.png

## Output

- Console output: Dataset statistics and hourly trip counts
- Image file: figure_hourly_demand.png (300 dpi)

## Data Source

The script expects NYC Yellow Taxi trip data in Parquet format. Data can be obtained from the NYC Taxi and Limousine Commission website.
