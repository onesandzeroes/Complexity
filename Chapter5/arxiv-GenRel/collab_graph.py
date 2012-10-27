import networkx

g = networkx.read_edgelist('CA-GrQc.txt')
print(len(g))
print(networkx.average_clustering(g))
