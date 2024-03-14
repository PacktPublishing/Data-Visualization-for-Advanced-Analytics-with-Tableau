# Create sample heatmap data.
# Imports
import pandas as pd
import numpy as np

# Set a seed for reproducibility
np.random.seed(42)

# Define products and months
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
months = ['January', 'February', 'March', 'April', 'May', 'June']

# Generate random sales data
sales_data = np.random.randint(100, 1000, size=(len(products), len(months)))

# Create a DataFrame with products as rows and months as columns
df = pd.DataFrame(sales_data, index=products, columns=months)

# Reset index to bring the 'products' into a column
df_reset = df.reset_index()

# Melt the DataFrame to get a long-format DataFrame suitable for Tableau
long_format_df = df_reset.melt(id_vars='index', var_name='Month', value_name='Sales')
long_format_df.rename(columns={'index': 'Product'}, inplace=True)

# Save the long-format DataFrame to an Excel file
long_format_df.to_excel("C:\\Usersheatmap_sales_data.xlsx", index=False)

long_format_df.head()
