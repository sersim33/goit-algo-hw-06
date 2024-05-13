import networkx as nx
import heapq

# Створення графа
G = nx.Graph()


# Додавання ребер з вагами
edges_with_weights = [('Lambeth North', 'Oxford Circus', {'weight': 5}), 
                      ('Paddington', 'Waterloo', {'weight': 10}), 
                      ('Willesden Junction', 'Wealdstone', {'weight': 8}), 
                      ('Waterloo', 'Charing Cross', {'weight': 7}), 
                      ('Charing Cross', 'Baker Street', {'weight': 6}), 
                      ('Willesden Junction', 'Charing Cross', {'weight': 9}), 
                      ('Waterloo', 'Oxford Circus', {'weight': 5}), 
                      ('Oxford Circus', 'Wealdstone', {'weight': 4})]

G.add_edges_from(edges_with_weights)

# реалізація Dijkstra
def dijkstra(graph, start):
    shortest = {vertex: float('infinity') for vertex in graph}
    shortest[start] = 0
    pq = [(0,start)]

    while pq:
        # print("shortest:", shortest)
        # print(pq)
        current_distance, current_vertex = heapq.heappop(pq)

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight['weight']
            if distance < shortest[neighbor]:
                shortest[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return shortest

# Виклик функції Dijkstra
result = dijkstra(G, 'Baker Street')

# Відсортуємо результати за відстанями
sorted_result = {k: v for k, v in sorted(result.items(), key=lambda item: item[1])}

# Виведемо відсортовані результати
print(sorted_result)