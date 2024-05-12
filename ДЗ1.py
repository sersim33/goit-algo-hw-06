import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add nodes
G.add_nodes_from(['Baker Street', 'Paddington', 'Waterloo', 'Willesden Junction', 'Charing Cross', 'Lambeth North', 'Oxford Circus', 'Wealdstone'])

# Add edges with weights - time
edges_with_weights = [('Lambeth North', 'Oxford Circus', {'weight': 5}), 
                      ('Paddington', 'Waterloo', {'weight': 10}), 
                      ('Willesden Junction', 'Wealdstone', {'weight': 8}), 
                      ('Waterloo', 'Charing Cross', {'weight': 7}), 
                      ('Charing Cross', 'Baker Street', {'weight': 6}), 
                      ('Willesden Junction', 'Charing Cross', {'weight': 9}), 
                      ('Waterloo', 'Oxford Circus', {'weight': 5}), 
                      ('Oxford Circus', 'Wealdstone', {'weight': 4})]

G.add_edges_from(edges_with_weights)

# Print nodes and edges
print("NODES:", len(G.nodes))
print(G.nodes())
print("EDGES:", len(G.edges))
print(G.edges(data=False))  # Include edge data (weights)


# Visualization of the graph
pos = nx.spring_layout(G)  # positions for all nodes
nx.draw(G, pos, with_labels=True, node_size=700, font_size=10, node_color='skyblue', edge_color='green')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})  # Include edge labels
plt.title("London Tube Network Graph")
plt.show()