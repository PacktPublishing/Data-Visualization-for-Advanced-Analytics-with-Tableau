import pandas as pd
import numpy as np

# Set the seed for reproducibility
np.random.seed(42)

# Number of data points
n_points = 200

# Generate the dataset
data = {
    "ID": np.arange(1, n_points + 1),
    "Category": np.random.choice(['A', 'B', 'C', 'D'], n_points),
    "Value": np.random.normal(loc=85, scale=5, size=n_points).astype(int),  # Assuming test scores around 85 with some variation
    "Time Period": np.random.choice(['Q1', 'Q2', 'Q3', 'Q4'], n_points),
    "Rating": np.random.choice([1, 2, 3, 4, 5], n_points)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the first few rows of the dataframe
df.head()

df.to_excel("C:\\sample_dot_plot.xlsx", index = False)