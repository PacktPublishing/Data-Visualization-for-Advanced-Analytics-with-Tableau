import pandas as pd
import numpy as np

# Function to create sample data
def create_sample_data(use_case):
    np.random.seed(42)  # For reproducibility

    if use_case == "Sales and Marketing":
        data = {
            "Region": np.random.choice(["North", "South", "East", "West"], 100),
            "Product": np.random.choice(["Product A", "Product B", "Product C"], 100),
            "Sales": np.random.randint(1, 100, 100)
        }
    elif use_case == "Finance":
        data = {
            "Category": np.random.choice(["Revenue", "Expenses", "Investments"], 100),
            "Month": np.random.choice(["January", "February", "March", "April", "May", "June"], 100),
            "Amount": np.random.randint(-1000, 1000, 100)
        }
    elif use_case == "Healthcare":
        data = {
            "Disease": np.random.choice(["Disease A", "Disease B", "Disease C"], 100),
            "Hospital": np.random.choice(["Hospital 1", "Hospital 2", "Hospital 3"], 100),
            "Outcomes": np.random.choice(["Recovered", "In Treatment", "Deceased"], 100)
        }
    elif use_case == "Logistics and Supply Chain":
        data = {
            "Route": np.random.choice(["Route 1", "Route 2", "Route 3"], 100),
            "Day": np.random.choice(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], 100),
            "Delivery Time (Hours)": np.random.randint(1, 24, 100)
        }
    elif use_case == "Real Estate":
        data = {
            "Location": np.random.choice(["Location 1", "Location 2", "Location 3"], 100),
            "Type": np.random.choice(["House", "Apartment", "Condo"], 100),
            "Value": np.random.randint(50000, 500000, 100)
        }
    elif use_case == "Environmental Science":
        data = {
            "Location": np.random.choice(["Area 1", "Area 2", "Area 3"], 100),
            "Month": np.random.choice(["January", "February", "March", "April"], 100),
            "Temperature (C)": np.random.randint(-10, 35, 100),
            "Pollution (AQI)": np.random.randint(0, 500, 100)
        }
    elif use_case == "Operational Data":
        data = {
            "Production Line": np.random.choice(["Line 1", "Line 2", "Line 3"], 100),
            "Metric": np.random.choice(["Efficiency", "Downtime", "Output"], 100),
            "Value": np.random.rand(100)
        }
    else:
        data = {}

    return pd.DataFrame(data)

# Use cases and filenames
use_cases = [
    "Sales and Marketing",
    "Finance",
    "Healthcare",
    "Logistics and Supply Chain",
    "Real Estate",
    "Environmental Science",
    "Operational Data"
]
file_names = [
    "sales_data.xlsx",
    "finance_data.xlsx",
    "healthcare_data.xlsx",
    "logistics_data.xlsx",
    "real_estate_data.xlsx",
    "environmental_data.xlsx",
    "operational_data.xlsx"
]

# Base file path
base_file_path = "C:\\chapter_five_datasets\\"

# Generate and save data
for use_case, file_name in zip(use_cases, file_names):
    df = create_sample_data(use_case)
    full_path = base_file_path + file_name
    df.to_excel(full_path, index=False)

print("Data saved successfully!")
