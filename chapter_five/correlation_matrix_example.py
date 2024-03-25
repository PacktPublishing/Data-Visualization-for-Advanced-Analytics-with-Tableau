# Sample correlation matrix example
# Imports
import pandas as pd
import numpy as np

# Set the seed for reproducibility
np.random.seed(42)

# Create a simulated dataset with 20 variables
n_variables = 20
n_observations = 100

# Generate random data
data = np.random.randn(n_observations, n_variables)

# Create a DataFrame and provide meaningful names to the variables
variables = [f"Var{i+1}" for i in range(n_variables)]
df = pd.DataFrame(data, columns=variables)

# Create logical groups among variables (for demonstration)
# Group 1: Var1 to Var7, Group 2: Var8 to Var14, Group 3: Var15 to Var20
groups = {'Finance': variables[0:7], 'Demographics': variables[7:14], 'User Engagement': variables[14:]}

# Calculate the correlation matrix and show preview
correlation_matrix = df.corr()
correlation_matrix.head()

# Convert to Excel for Tableau import
df.to_excel("filepath_goes_here.xlsx")

