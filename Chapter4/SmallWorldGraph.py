#! /usr/bin/env python3
import random
import matplotlib.pyplot as pyplot
import networkx as nx


class SmallWorldGraph(nx.Graph):
    def __init__(self, n, k, p):
        nx.Graph.__init__(self)
        create = nx.watts_strogatz_graph(n, k, p)
        self.add_nodes_from(create.nodes())
        self.add_edges_from(create.edges())

    def rewire(self, p):
        """
        Rewire the graph a la Watts and Strogatz, so that each edge gets
        rewired with probability p to a random node
        """
        nodes = self.nodes()
        edges = self.edges_iter()
        for e in edges:
            roll = random.random()
            if roll < p:
                found_new_end = False
                while not found_new_end:
                    edge_start = e[0]
                    old_end = e[1]
                    new_end = random.choice(nodes)
                    if not new_end == edge_start:
                        if not new_end in self[edge_start].keys():
                            self.remove_edge(edge_start, old_end)
                            self.add_edge(edge_start, new_end)
                            found_new_end = True

    def clustering_coefficient_node(self, node):
        kv = len(self.neighbors(node))
        max_connects = kv * (kv - 1) / 2
        all_neighbors = list(self.neighbors(node))
        found_edges = set()
        for neighbor in all_neighbors:
            outs = self.neighbors(neighbor)
            for out in outs:
                if out in all_neighbors:
                    # Don't want to count the same edge twice
                    if (out, neighbor) not in found_edges:
                        found_edges.add((neighbor, out))
        cv = len(found_edges) / max_connects
        return cv

    def clustering_coefficient(self):
        cvs = []
        for node in self.nodes():
            cvs.append(self.clustering_coefficient_node(node))
        mean_c = sum(cvs) / len(cvs)
        return mean_c


def rewire(graph, p):
    """
    Rewire a graph a la Watts and Strogatz, so that each edge gets rewired
    with probability p to a random node
    """
    nodes = graph.nodes()
    edges = graph.edges_iter()
    for e in edges:
        roll = random.random()
        if roll < p:
            found_new_end = False
            while not found_new_end:
                edge_start = e[0]
                old_end = e[1]
                new_end = random.choice(nodes)
                if not new_end in graph[edge_start].keys():
                    graph.remove_edge(edge_start, old_end)
                    graph.add_edge(edge_start, new_end)
                    found_new_end = True

if __name__ == '__main__':
    g = SmallWorldGraph(500, 20, 0)
    test_node = g.nodes()[0]
    print(g.clustering_coefficient_node(test_node))
    print(nx.clustering(g, test_node))
    print(g.clustering_coefficient())
    print(nx.average_clustering(g))
    g.rewire(0.5)
    print(g.clustering_coefficient_node(test_node))
    print(nx.clustering(g, test_node))
    print(g.clustering_coefficient())
    print(nx.average_clustering(g))
    # nx.draw_circular(g)
    # pyplot.show()
    # g.rewire(0.5)
    # nx.draw_circular(g)
    # pyplot.show()

    # Saving to .dot files/pngs requires pygraphviz, which isn't available
    # yet for python3, should work fine when run using python2 though
    # g = nx.watts_strogatz_graph(20, 4, 0)
    # A = nx.to_agraph(g)
    # A.layout(prog='circo')
    # A.draw('regular.png')
    # rewire(g, 0.2)
    # A2 = nx.to_agraph(g)
    # A2.layout(prog='circo')
    # A2.draw('rewired.png')

