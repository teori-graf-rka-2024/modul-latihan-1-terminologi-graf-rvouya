import graph as g

# non-tree
# edge_list = [(1, 2), (2,3), (3,5), (1,4), (1,5)]

# tree
# edge_list = [
#     (0, 1), (0, 2),
#     (1, 3), (1, 4),
#     (2, 5), (2, 6),
#     (4, 7), (4, 8)
# ]

# edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (2, 5)]
edges = [(1, 2), (2, 3), (3, 4)]

G = g.create_graph(edges)
print(len(G.nodes))
print(len(G.edges))
print(g.get_degree(G, 2))
print(g.dfs_traversal(G, 1))
print(g.bfs_traversal(G, 1))
print(g.find_shortest_path(G, 1, 4)) 
g.visualize_graph(G)
