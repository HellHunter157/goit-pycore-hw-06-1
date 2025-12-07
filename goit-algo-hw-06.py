import networkx as nx
import matplotlib.pyplot as plt
import random
from collections import deque




G = nx.Graph()
stations = ["A", "B", "C", "D", "E", "F"]
edges = [
    ("A", "B"), ("B", "C"), ("C", "D"),
    ("A", "E"), ("E", "F"), ("F", "D"),
    ("B", "E")
]
# G.add_nodes_from(stations)
# G.add_edges_from(edges)
# plt.figure(figsize=(6, 4))
# pos = nx.spring_layout(G)
# nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=12)
# plt.title("City Transport Network")
# plt.show()
# print("Number of nodes:", G.number_of_nodes())
# print("Number of edges:", G.number_of_edges())
# print("\nDegrees of nodes:")
# for node, degree in G.degree():
#     print(f"{node}: {degree}")













# def bfs(G, start, goal):
#     visited = set([start])
#     queue = deque([[start]])
#     while queue:
#         path = queue.popleft()
#         node = path[-1]
#         if node == goal:
#             return path
#         for neighbor in G.neighbors(node):
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 queue.append(path + [neighbor])
# def dfs(G, start, goal):
#     visited = set([start])
#     stack = [[start]]
#     while stack:
#         path = stack.pop()
#         node = path[-1]
#         if node == goal:
#             return path
#         for neighbor in G.neighbors(node):
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 stack.append(path + [neighbor])
# bfs_path = bfs(G, "A", "D")
# dfs_path = dfs(G, "A", "D")
# print("BFS path from A to D:", bfs_path)
# print("DFS path from A to D:", dfs_path)














for u, v in edges:
    weight = random.randint(1, 10)
    G.add_edge(u, v, weight=weight)
dijkstra_paths = dict(nx.all_pairs_dijkstra_path(G))
dijkstra_lengths = dict(nx.all_pairs_dijkstra_path_length(G))
print("\nDijkstra shortest paths:")
for start, targets in dijkstra_paths.items():
    for end, path in targets.items():
        print(f"{start} → {end}: {path}")
print("\nDijkstra path lengths (total weights):")
for start, targets in dijkstra_lengths.items():
    for end, length in targets.items():
        print(f"{start} → {end}: {length}")
