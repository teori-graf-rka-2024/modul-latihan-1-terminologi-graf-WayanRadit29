from graph import *

# 1. Definisikan edges
edges = [(1, 2), (1, 3), (2, 4), (3, 4), (3, 5), (4, 5)]
G = create_graph(edges)

# 2. Hitung degree
print("Degree node 3:", get_degree(G, 3))

# 3. DFS Traversal
print("DFS Traversal dari node 1:", dfs_traversal(G, 1))

# 4. BFS Traversal
print("BFS Traversal dari node 1:", bfs_traversal(G, 1))

# 5. Shortest Path
print("Shortest path dari 1 ke 5:", find_shortest_path(G, 1, 5))

# 6. Visualisasi graf
visualize_graph(G, "graph_output.png")
