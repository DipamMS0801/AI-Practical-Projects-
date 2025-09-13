import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Your original graph
graph = {
    'Alice': ['Bob', 'Charlie'],
    'Bob': ['Alice', 'David', 'Eve'],
    'Charlie': ['Alice', 'Faythe'],
    'David': ['Bob'],
    'Eve': ['Bob', 'Faythe'],
    'Faythe': ['Charlie', 'Eve']
}

# Convert your dict graph to a NetworkX graph
G = nx.Graph()
for person, friends in graph.items():
    for friend in friends:
        G.add_edge(person, friend)

def bfs_degree(graph, start, target):
    visited = set()
    queue = deque([(start, 0)])  # (person, degree)
    while queue:
        current, degree = queue.popleft()
        if current == target:
            return degree
        if current not in visited:
            visited.add(current)
            for neighbor in graph.get(current, []):
                queue.append((neighbor, degree + 1))
    return -1

def mutual_connections(graph, person1, person2):
    return list(set(graph.get(person1, [])) & set(graph.get(person2, [])))

def friend_suggestions(graph, person):
    suggestions = set()
    for friend in graph.get(person, []):
        for fof in graph.get(friend, []):
            if fof != person and fof not in graph[person]:
                suggestions.add(fof)
    return list(suggestions)

def visualize_graph(G, highlight_nodes=None, highlight_edges=None):
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(8,6))

    # Draw all nodes and edges faintly
    nx.draw_networkx_nodes(G, pos, node_color='lightblue')
    nx.draw_networkx_edges(G, pos, edge_color='lightgray')
    nx.draw_networkx_labels(G, pos, font_size=10)

    # Highlight nodes
    if highlight_nodes:
        nx.draw_networkx_nodes(G, pos, nodelist=highlight_nodes, node_color='orange')

    # Highlight edges
    if highlight_edges:
        nx.draw_networkx_edges(G, pos, edgelist=highlight_edges, edge_color='red', width=2)

    plt.axis('off')
    plt.show()

def highlight_path(graph, start, target):
    # BFS to find shortest path
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        current, path = queue.popleft()
        if current == target:
            return path
        if current not in visited:
            visited.add(current)
            for neighbor in graph.get(current, []):
                queue.append((neighbor, path + [neighbor]))
    return []



while True:
    print("\n1. Degree of separation")
    print("2. Mutual connections")
    print("3. Friend suggestions")
    print("4. Visualize entire network")
    print("5. Exit")
    choice = input("Enter choice: ").strip()

    if choice == '1':
        a = input("Enter person 1: ").strip()
        b = input("Enter person 2: ").strip()
        if a not in graph or b not in graph:
            print("One or both persons are not in the network. Try again.")
            continue
        degree = bfs_degree(graph, a, b)
        print(f"Degree of separation between {a} and {b}: {degree}")

        if degree != -1:
            path = highlight_path(graph, a, b)
            print("Shortest path:", " -> ".join(path))
            edges_to_highlight = [
                (path[i], path[i+1]) if (path[i], path[i+1]) in G.edges else (path[i+1], path[i])
                for i in range(len(path)-1)
            ]
            visualize_graph(G, highlight_nodes=path, highlight_edges=edges_to_highlight)
        else:
            print("No connection found.")

    elif choice == '2':
        a = input("Enter person 1: ").strip()
        b = input("Enter person 2: ").strip()
        if a not in graph or b not in graph:
            print("One or both persons are not in the network. Try again.")
            continue
        mutuals = mutual_connections(graph, a, b)
        print(f"Mutual friends between {a} and {b}: {mutuals}")
        visualize_graph(G, highlight_nodes=[a, b] + mutuals)

    elif choice == '3':
        a = input("Enter person name: ").strip()
        if a not in graph:
            print(f"{a} is not in the network. Try again.")
            continue
        suggestions = friend_suggestions(graph, a)
        print(f"Friend suggestions for {a}: {suggestions}")
        visualize_graph(G, highlight_nodes=[a] + suggestions)

    elif choice == '4':
        visualize_graph(G)

    elif choice == '5':
        print("Exiting program.")
        break

    else:
        print("Invalid choice, try again.")

