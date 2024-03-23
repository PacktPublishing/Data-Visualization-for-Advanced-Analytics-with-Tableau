# Sample data generated for financial analytics dashboard.
# Imports
import pandas as pd
import numpy as np

# Setting a seed for reproducibility
np.random.seed(42)

# Defining the quarters
quarters = ['Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023', 'Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024']

# Generating random data
revenue = np.random.uniform(750000, 1500000, size=len(quarters))
expenses = revenue * np.random.uniform(0.5, 0.8, size=len(quarters))
profit_margin = (revenue - expenses) / revenue * 100
client_acquisition = np.random.randint(20, 50, size=len(quarters))

# Investment performance by asset class
equities_performance = np.random.uniform(5, 15, size=len(quarters))
bonds_performance = np.random.uniform(2, 7, size=len(quarters))
commodities_performance = np.random.uniform(-3, 10, size=len(quarters))

# Creating a DataFrame
df = pd.DataFrame({
    'Quarter': quarters,
    'Revenue': revenue,
    'Expenses': expenses,
    'Profit Margin (%)': profit_margin,
    'New Clients': client_acquisition,
    'Equities ROI (%)': equities_performance,
    'Bonds ROI (%)': bonds_performance,
    'Commodities ROI (%)': commodities_performance
})

df

# Convert and save dataframe as Excel file to local machine (optional)
df.to_excel("C:\\chapter_threesample_data.xlsx")
