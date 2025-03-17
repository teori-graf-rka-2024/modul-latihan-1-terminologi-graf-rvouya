import networkx as nx
import matplotlib.pyplot as plt

def create_graph(edges: list[tuple[int, int]]) -> nx.Graph:
    return (nx.Graph(edges))

def get_degree(G: nx.Graph, node: int) -> int:
    return G.degree[node]

def dfs_traversal(G: nx.Graph, start: int) -> list[int]:
    return list(nx.dfs_preorder_nodes(G, start))

def bfs_traversal(G: nx.Graph, start: int) -> list[int]:
    return list(nx.bfs_tree(G, start))

def find_shortest_path(G: nx.Graph, source: int, target: int) -> list[int]:
    return nx.shortest_path(G, source, target)

def visualize_graph(G: nx.Graph) -> None:
    nx.draw(G, with_labels=True)
    plt.savefig("graph.png")
    plt.show()
