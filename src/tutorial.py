import graph as g

# non-tree
# edge_list = [(1, 2), (2,3), (3,5), (1,4), (1,5)]
 WOIII
# tree
edge_list = [
    (0, 1), (0, 2),
    (1, 3), (1, 4),
    (2, 5), (2, 6),
    (4, 7), (4, 8)
]

G = g.create_graph(edge_list)
print(g.get_degree(G, 1))
print(g.dfs_traversal(G, 1))
print(g.bfs_traversal(G, 1))
print(g.find_shortest_path(G, 0, 6)) # gimana caranya supaya tidak ketemu? kan edge_list pasti ada pasangan dong??
g.visualize_graph(G)