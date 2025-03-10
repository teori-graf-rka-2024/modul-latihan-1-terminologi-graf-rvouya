import networkx as nx
import matplotlib.pyplot as plt

G = nx.graph()

def create_graph(edges: list[tuple[int, int]]) -> nx.Graph:
    G.add_edges_from(edges)

def get_degree(G: nx.Graph, node: int) -> int:
    return dict(G.degree)[node]

def dfs_traversal(G: nx.Graph, start: int) -> list[int]:
    return nx.dfs_preorder_nodes(G, start)

def bfs_traversal(G: nx.Graph, start: int) -> list[int]:
    return nx.bfs_edges(G, start)

def find_shortest_path(G: nx.Graph, source: int, target: int) -> list[int]:
    return nx.shortest_path(G, source, target)

def visualize_graph(G: nx.Graph) -> None:
    nx.draw_circular(G, with_labels=True)
    plt.show()