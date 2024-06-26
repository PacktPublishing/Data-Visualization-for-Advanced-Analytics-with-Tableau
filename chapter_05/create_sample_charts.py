import pandas as pd
import random

# Network Graph Dataset
# Nodes represent individuals, edges represent some form of relationship
nodes = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eva', 'Frank']
edges = [(random.choice(nodes), random.choice(nodes)) for _ in range(10)]

network_df = pd.DataFrame(edges, columns=['Source', 'Target'])
network_df.to_excel("C:\\chapter_five_datasets\\network_graph_data.xlsx", index=False)

# Sankey Diagram Dataset
# Show flow from one category to another, e.g., stages in a process
stages = ['Stage 1', 'Stage 2', 'Stage 3', 'Stage 4']
flows = [(random.choice(stages), random.choice(stages), random.randint(1, 100)) for _ in range(10)]

sankey_df = pd.DataFrame(flows, columns=['Source', 'Target', 'Value'])
sankey_df.to_excel("C:\\sankey_diagram_data.xlsx", index=False)

# Treemap Dataset
# Hierarchical data, e.g., department, teams, and individuals with some values
departments = ['HR', 'Tech', 'Marketing']
teams = ['Team 1', 'Team 2', 'Team 3']
individuals = ['Person A', 'Person B', 'Person C']

tree_data = []
for department in departments:
    for team in teams:
        for individual in individuals:
            value = random.randint(1, 100)
            tree_data.append([department, team, individual, value])

treemap_df = pd.DataFrame(tree_data, columns=['Department', 'Team', 'Individual', 'Value'])
treemap_df.to_excel("C:\\treemap_data.xlsx", index=False)

print("Datasets created: network_graph_data.xlsx, sankey_diagram_data.xlsx, treemap_data.xlsx")
