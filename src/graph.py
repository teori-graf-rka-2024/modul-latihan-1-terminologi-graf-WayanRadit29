
import networkx as nx
import matplotlib.pyplot as plt

def create_graph(edges):
    G = nx.Graph()
    G.add_edges_from(edges)
    return G

def get_degree(G, node):
    if node not in G:
        raise ValueError("Node tidak ada dalam graf.")
    return G.degree[node]

def dfs_traversal(G, start):
    if start not in G:
        raise ValueError("Node tidak ada dalam graf.")
    return list(nx.dfs_preorder_nodes(G, start))

def bfs_traversal(G, start):
    if start not in G:
        raise ValueError("Node tidak ada dalam graf.")
    return list(nx.bfs_edges(G, start))

def find_shortest_path(G, source, target):
    if source not in G or target not in G:
        raise ValueError("Source atau target tidak ada dalam graf.")
    return nx.shortest_path(G, source=source, target=target)

def visualize_graph(G, filename="graph.png"): #Kita coba filenamenya isi timestamp pas dibuat
    plt.figure(figsize=(8, 6))
    nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)
    plt.savefig(filename)
    print(f"Graf disimpan sebagai {filename}")

    