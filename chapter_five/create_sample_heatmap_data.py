import pandas as pd
import numpy as np

# Generate a sample dataset for a heatmap
np.random.seed(42)  # For reproducible results

# Assuming we're creating a dataset representing sales data across different products and months
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
months = ['January', 'February', 'March', 'April', 'May', 'June']

# Generate random sales data
sales_data = np.random.randint(100, 1000, size=(len(products), len(months)))

# Create a DataFrame
heatmap_df = pd.DataFrame(sales_data, index=products, columns=months)

# Save the dataset to an Excel file
heatmap_df.to_excel("/mnt/data/heatmap_sales_data.xlsx")

heatmap_df
