import pandas as pd  # Data analysis library

df = pd.read_parquet("yellow_tripdata_2019-08.parquet")  # Load taxi data

print(df.head())  # Print first 5 rows
print(df.shape)  # Check data shape
print(df.columns)  # Check column names

df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])  # Convert to datetime
df["hour"] = df["tpep_pickup_datetime"].dt.hour  # Extract hour
df["date"] = df["tpep_pickup_datetime"].dt.date  # Extract date

print(df[["tpep_pickup_datetime", "hour", "date"]].head())  # Check time columns

hourly_counts = df.groupby("hour").size()  # Count trips by hour

print(hourly_counts)  # Print results

import matplotlib.pyplot as plt  # Visualization library

plt.figure()  # Create figure
hourly_counts.plot(color='orange')  # Plot line graph (orange color)
plt.xlabel("Hour of Day")  # X-axis label
plt.ylabel("Number of Trips")  # Y-axis label
plt.title("Hourly Distribution of NYC Yellow Taxi Trips (Aug 2019)")  # Title
plt.tight_layout()  # Adjust layout
plt.savefig("figure_hourly_demand.png", dpi=300)  # Save figure
plt.show()  # Display plot
