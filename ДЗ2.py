from collections import deque
import networkx as nx

def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ')  # Відвідуємо вершину
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


def bfs_recursive(graph, queue, visited=None):
    # Перевіряємо, чи існує множина відвіданих вершин, якщо ні, то ініціалізуємо нову
    if visited is None:
        visited = set()
    # Якщо черга порожня, завершуємо рекурсію
    if not queue:
        return
    # Вилучаємо вершину з початку черги
    vertex = queue.popleft()
    # Перевіряємо, чи відвідували раніше дану вершину
    if vertex not in visited:
        # Якщо не відвідували, друкуємо вершину
        print(vertex, end=" ")
        # Додаємо вершину до множини відвіданих вершин.
        visited.add(vertex)
        # Додаємо невідвіданих сусідів даної вершини в кінець черги.
        queue.extend(set(graph[vertex]) - visited)
    # Рекурсивний виклик функції з тією ж чергою та множиною відвіданих вершин
    bfs_recursive(graph, queue, visited)

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

# Виклик функції DFS
print("DFS")
dfs_recursive(G, 'Waterloo')
print("\n")
print("BFS")
# Запуск рекурсивного алгоритму BFS
bfs_recursive(G, deque(['Waterloo']))