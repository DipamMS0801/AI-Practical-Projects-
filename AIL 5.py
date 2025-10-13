import heapq
import networkx as nx
import matplotlib.pyplot as plt

def prim_mst(graph, start=0):
    visited = set([start])
    edges = [(weight, start, v) for v, weight in graph[start]]
    heapq.heapify(edges)

    mst_edges = []
    total_weight = 0

    while edges:
        weight, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst_edges.append((u, v, weight))
            total_weight += weight

            for to_neighbor, edge_weight in graph[v]:
                if to_neighbor not in visited:
                    heapq.heappush(edges, (edge_weight, v, to_neighbor))
            
            if len(visited) == len(graph):
                break
    
    return mst_edges, total_weight


# Graph representation (undirected)
graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8)],
    2: [(1, 3), (3, 7)],
    3: [(0, 6), (1, 8), (2, 7)],
}

# Run Prim's algorithm
mst, total = prim_mst(graph, start=0)

# Display MST edges and total weight
print("Edges in the MST:")
for u, v, w in mst:
    print(f"{u} - {v} (weight {w})")
print(f"Total weight of MST: {total}")

# Create graph using NetworkX
G = nx.Graph()
for u in graph:
    for v, w in graph[u]:
        if not G.has_edge(u, v):  # Avoid duplicate edges
            G.add_edge(u, v, weight=w)

# Draw full graph
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx_nodes(G, pos, node_size=600, node_color='lightblue')
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
nx.draw_networkx_edges(G, pos, alpha=0.4, edge_color='gray')

# Draw edge labels
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Highlight MST edges in red
mst_edges = [(u, v) for u, v, w in mst]
nx.draw_networkx_edges(G, pos, edgelist=mst_edges, edge_color='red', width=3)

plt.title("Graph and Prim's MST (Red Edges)")
plt.axis('off')
plt.show()
