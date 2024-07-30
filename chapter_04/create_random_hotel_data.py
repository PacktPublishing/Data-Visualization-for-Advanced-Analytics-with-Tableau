# Create hotel dataset for chapter four.
# Imports
import pandas as pd
import numpy as np
import random

# Setting seed for reproducibility
np.random.seed(42)

# Define the number of records
num_records = 1000

# Create a date range
date_range = pd.date_range(start='2021-01-01', end='2021-12-31', periods=num_records)

# Hotel names
hotels = ['Hotel California', 'Grand Budapest', 'Overlook Hotel', 'The Great Northern', 'Bates Motel']

# Room types
room_types = ['Single', 'Double', 'Suite', 'Penthouse']

# Create random data
data = {
    'Date': np.random.choice(date_range, size=num_records),
    'Hotel Name': np.random.choice(hotels, size=num_records),
    'Room Type': np.random.choice(room_types, size=num_records),
    'Number of Guests': np.random.randint(1, 5, size=num_records),
    'Duration (Days)': np.random.randint(1, 15, size=num_records),
    'Price per Night ($)': np.random.randint(50, 500, size=num_records),
    'Total Revenue ($)': 0,  # Placeholder, to be calculated
    'City': np.random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'], size=num_records),
    'Rating': np.random.choice([1, 2, 3, 4, 5], size=num_records, p=[0.05, 0.1, 0.4, 0.3, 0.15]),
    'Booking Source': np.random.choice(['Direct', 'Online Travel Agent', 'Walk-in', 'Corporate'], size=num_records)
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Calculate total revenue
df['Total Revenue ($)'] = df['Price per Night ($)'] * df['Duration (Days)']

# Introduce some anomalies/outliers
outlier_indices = np.random.choice(df.index, size=int(num_records * 0.01), replace=False)
df.loc[outlier_indices, 'Price per Night ($)'] = df.loc[outlier_indices, 'Price per Night ($)'] * np.random.randint(5, 10)

# Display the DataFrame
df.head(), df.describe(include='all', datetime_is_numeric=True)

# Save dataset to local machine for clarity (optional)
df.to_excel("C:\\Users\\chapter_four_datasets\\hotel_dataset.xlsx", index = False)