import networkx as nx
import matplotlib.pyplot as plt
import random
from collections import deque

nodes = ["A", "B", "C", "D", "E", "F"]
G = nx.Graph()
G.add_nodes_from(nodes)

for a in nodes:
    for b in nodes:
        if a < b and random.random() < 0.45:
            G.add_edge(a, b)

plt.figure(figsize=(6, 4))
pos = nx.spring_layout(G, seed=7)
nx.draw(G, pos, with_labels=True, node_size=700)
plt.show()

print("Nodes:", len(G.nodes()))
print("Edges:", len(G.edges()))
print("Degrees:")
for n, d in G.degree():
    print(n, d)

def bfs(G, s, g):
    q = deque([[s]])
    seen = {s}
    while q:
        p = q.popleft()
        v = p[-1]
        if v == g:
            return p
        for x in G[v]:
            if x not in seen:
                seen.add(x)
                q.append(p + [x])

def dfs(G, s, g):
    st = [[s]]
    seen = {s}
    while st:
        p = st.pop()
        v = p[-1]
        if v == g:
            return p
        for x in G[v]:
            if x not in seen:
                seen.add(x)
                st.append(p + [x])

print("BFS A→D:", bfs(G, "A", "D"))
print("DFS A→D:", dfs(G, "A", "D"))

for u, v in G.edges():
    G[u][v]['weight'] = random.randint(1, 15)

paths = dict(nx.all_pairs_dijkstra_path(G))
dist = dict(nx.all_pairs_dijkstra_path_length(G))

for a in paths:
    for b in paths[a]:
        print(a, "→", b, ":", paths[a][b], " cost:", dist[a][b])
