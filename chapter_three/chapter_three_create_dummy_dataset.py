# Create dummy dataset with python for chapter three pictures.
# Imports
import pandas as pd
import numpy as np

# Define the date range (two years of data)
dates = pd.date_range(start='2022-01-01', end='2023-12-31')  

# Create random data
sales = np.random.randint(100, 5000, size=len(dates))  # Random sales figures between 100 and 5000
expenses = np.random.randint(50, 2500, size=len(dates))  # Random expenses figures between 50 and 2500
regions = np.random.choice(['North', 'South', 'East', 'West'], size=len(dates))  # Random regions
products = np.random.choice(['Product A', 'Product B', 'Product C', 'Product D'], size=len(dates))  # Random products

# Create the DataFrame
df = pd.DataFrame({
    'Date': dates,
    'Sales': sales,
    'Expenses': expenses,
    'Region': regions,
    'Product': products
})

# Save the DataFrame to an Excel file for Tableau demo purposes
df.to_excel('dummy_dataset.xlsx', index=False)
