# /usr/bin/env python3
"""Implements graphs as a dictionary of dictionaries"""

class Graph(dict):
    # Textbook had vs=[] as the default value. Isn't this the mutable default
    # argument problem?
    def __init__(self, vs=[], es=[]):
        """Create a new graph. (vs) is a list of vertices;
        (es) is a list of edges."""
        for v in vs:
            self.add_vertex(v)
        for e in es:
            self.add_edge(e)
    def add_vertex(self, v):
        """Add (v) to the graph"""
        self[v] = {}
    def add_edge(self, e):
        """Add (e) to the graph by adding an entry in both directions.

        If there is already an edge connecting these Vertices, the new edge
        replaces it.
        """
        v, w = e
        self[v][w] = e
        self[w][v] = e

class Vertex:
    def __init__(self, label=''):
        self.label = label
    def __repr__(self):
        return 'Vertex({0})'.format(self.label)
    __str__ = __repr__

class Edge(tuple):
    # Need to use __new__ instead of __init__ because it's inheriting from
    # tuple, and tuples are immutable, so you can't modify the individual
    # elements in the __init__() call
    def __new__(cls, e1, e2):
        return tuple.__new__(cls, (e1, e2))
    def __repr__(self):
        return 'Edge({0}, {1})'.format(repr(self[0]), repr(self[1]))
    __str__ = __repr__

if __name__ == '__main__':
    v = Vertex('v')
    w = Vertex('w')
    e = Edge(v, w)
    print(e)
    g = Graph([v, w], [e])
    print(g)
