import networkx as nx

with open("input.in") as f:
    ns = [tuple(map(int, l.split(","))) for l in f.read().strip().split("\n")]
G = nx.grid_2d_graph(71, 71)
for i, p in enumerate(ns):
    G.remove_node(p)
    if i == 1023:
        print("Part 1 solution:", nx.shortest_path_length(G, (0, 0), (70, 70)))
    elif not nx.has_path(G, (0, 0), (70, 70)):
        print("Part 2 solution:", p)
        break
