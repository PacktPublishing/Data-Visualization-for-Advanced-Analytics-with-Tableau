# Sample data for network graphs.
# Imports
import pandas as pd
import random

# Base file path where the Excel files will be saved (optional)
base_path = "C:\\tableau\\"

# Function to generate a social network dataset
def generate_social_network():
    users = [f"User_{i}" for i in range(1, 101)]
    friendships = [(random.choice(users), random.choice(users)) for _ in range(200)]
    weights = [random.randint(1, 10) for _ in range(200)]  # Generate random weights
    df = pd.DataFrame(friendships, columns=['User', 'Friend'])
    df['Weight'] = weights  # Add the weights as a third column
    df.to_excel(base_path + 'social_network.xlsx', index=False)

# Function to generate a transportation network dataset
def generate_transport_network():
    locations = [f"Location_{i}" for i in range(1, 21)]
    routes = [(random.choice(locations), random.choice(locations)) for _ in range(50)]
    df = pd.DataFrame(routes, columns=['Location', 'Connection'])
    df.to_excel(base_path + 'transport_network.xlsx', index=False)

# Function to generate a biological and genetic network dataset
def generate_bio_network():
    proteins = [f"Protein_{i}" for i in range(1, 51)]
    interactions = [(random.choice(proteins), random.choice(proteins)) for _ in range(100)]
    df = pd.DataFrame(interactions, columns=['Protein', 'Interaction'])
    df.to_excel(base_path + 'biological_network.xlsx', index=False)

# Function to generate a corporate organizational structure dataset
def generate_org_structure():
    employees = [f"Employee_{i}" for i in range(1, 101)]
    reports = [(random.choice(employees), random.choice(employees)) for _ in range(150)]
    df = pd.DataFrame(reports, columns=['Employee', 'Reports_To'])
    df.to_excel(base_path + 'organizational_structure.xlsx', index=False)

# Function to generate an internet and web network dataset
def generate_web_network():
    web_pages = [f"Page_{i}" for i in range(1, 101)]
    hyperlinks = [(random.choice(web_pages), random.choice(web_pages)) for _ in range(200)]
    df = pd.DataFrame(hyperlinks, columns=['Page', 'Hyperlink'])
    df.to_excel(base_path + 'web_network.xlsx', index=False)

# Function to generate a criminal and law enforcement network dataset
def generate_crime_network():
    suspects = [f"Suspect_{i}" for i in range(1, 51)]
    connections = [(random.choice(suspects), random.choice(suspects)) for _ in range(100)]
    df = pd.DataFrame(connections, columns=['Suspect', 'Connection'])
    df.to_excel(base_path + 'crime_network.xlsx', index=False)

if __name__ == "__main__":
    generate_social_network()
    generate_transport_network()
    generate_bio_network()
    generate_org_structure()
    generate_web_network()
    generate_crime_network()
    print("All datasets have been generated and saved as Excel files in the specified directory.")
