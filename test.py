import pandas as pd

# Provide the file path to your CSV file
file_path = "London tube lines.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Select the first 50 rows (stations)
df = df.head(50)

print(df)

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Adding nodes (tube lines)
tube_lines = set(df["Tube Line"])  # Get unique tube lines
for line in tube_lines:
    G.add_node(line)

# Adding edges (stations)
for index, row in df.iterrows():
    G.add_edge(row["From Station"], row["To Station"], line=row["Tube Line"])

print(G.nodes()) 
print("EDGES:")
print(G.edges()) 

neighbors_of_C2C = G["C2C"]
print(neighbors_of_C2C) 

# Visualization of the graph
pos = nx.spring_layout(G)  # positions for all nodes
nx.draw(G, with_labels=True, node_size=700, font_size=7, node_color='skyblue', edge_color='gray')
plt.title("London Tube Network Graph")
plt.show()