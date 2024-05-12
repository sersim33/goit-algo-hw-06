import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання станцій і часу
edges_with_weights = [('Lambeth North', 'Oxford Circus', {'weight': 5}), 
                      ('Paddington', 'Waterloo', {'weight': 10}), 
                      ('Willesden Junction', 'Wealdstone', {'weight': 8}), 
                      ('Waterloo', 'Charing Cross', {'weight': 7}), 
                      ('Charing Cross', 'Baker Street', {'weight': 6}), 
                      ('Willesden Junction', 'Charing Cross', {'weight': 9}), 
                      ('Waterloo', 'Oxford Circus', {'weight': 5}), 
                      ('Oxford Circus', 'Wealdstone', {'weight': 4})]

G.add_edges_from(edges_with_weights)

# Застосування алгоритму Дейкстри
shortest_paths = nx.single_source_dijkstra_path(G, source='Baker Street')
shortest_path_lengths = nx.single_source_dijkstra_path_length(G, source='Baker Street')
print(shortest_paths)  # виведе найкоротші шляхи по часу від вузла 'Baker Street' до всіх інших вузлів
print("Shortest_path_lengths:")
print(shortest_path_lengths)  # виведе час найкоротших шляхів від вузла 'Baker Street' до всіх інших вузлів

# Visualization of the graph
pos = nx.spring_layout(G)  # positions for all nodes
nx.draw(G, pos, with_labels=True, node_size=700, font_size=9, node_color='skyblue', edge_color='gray')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})  # Include edge labels
plt.title("London Tube Network Graph")
plt.show()

