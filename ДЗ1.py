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

degree_centrality = nx.degree_centrality(G)  
closeness_centrality = nx.closeness_centrality(G)  
betweenness_centrality = nx.betweenness_centrality(G)  
is_connected = nx.is_connected(G)

# Print nodes and edges
print("NODES:", len(G.nodes))
print(G.nodes())
print("EDGES:", len(G.edges))
print(G.edges(data=True))  # Include edge data (weights)
print("Аналіз графу щодо ступіня центральності, близькості та посередництва")  
print(degree_centrality)
print(closeness_centrality)
print(betweenness_centrality)
print(is_connected)

# Visualization of the graph
pos = nx.spring_layout(G)  # positions for all nodes
nx.draw(G, pos, with_labels=True, node_size=700, font_size=10, node_color='skyblue', edge_color='green')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})  # Include edge labels
plt.title("London Tube Network Graph")
plt.show()