from __future__ import division
import random
import itertools
from Graph import Graph, Vertex
import string
from textwrap import dedent


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


def phase_change_sim(nodes, iterations=20, breaks=20):
    # Store results in a dictionary with p values as keys, and the proportion
    # of connected graphs as values
    results = {}
    if nodes > 52:
        print("Too many nodes! 52 is the maximum for now")
        return None
    verts = [Vertex(char) for char in string.ascii_letters]
    for p in xrange(1, breaks):
        # use __future__ division because the python2 version is too
        # shitty
        p = p / breaks
        num_connected = 0
        for i in range(iterations):
            g = RandomGraph(verts[:nodes], [])
            g.add_random_edges(p)
            if g.is_connected():
                num_connected += 1
        results[p] = num_connected / iterations
    # Print results
    print(dedent(
    """
    Nodes: {nodes}
    Results:
    --------

    """.format(nodes=nodes)
    )
    )
    sorted_res = [res for res in results]
    sorted_res.sort()
    for res in sorted_res:
        print(str(res) + ": " + str(results[res]))

if __name__ == '__main__':
    for i in range(2, 10):
        phase_change_sim(i)
