import random
import itertools
from Graph import Graph


class RandomGraph(Graph):
    """
    Implements the Erdos-Renyi model, where for a graph
    G(n,p), the probability is p that there will be an
    edge between any two nodes
    """

    def add_random_edges(self, p):
        verts = self.vertices()
        pairs = itertools.combinations(verts, 2)
        for pair in pairs:
            dice_roll = random.random()
            if dice_roll < p:
                self.add_edge(pair)
