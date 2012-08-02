""" 
Code example from Complexity and Computation, a book about
exploring complexity science with Python.  Available free from

http://greenteapress.com/complexity

Copyright 2011 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
"""
import random

class Vertex:
    """A Vertex is a node in a graph."""

    def __init__(self, label=''):
        self.label = label

    def __repr__(self):
        """Returns a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Vertex({0})'.format(repr(self.label))

    __str__ = __repr__
    """The str and repr forms of this object are the same."""

class Edge(tuple):
    """An Edge is a list of two vertices."""

    def __new__(cls, *vs):
        """The Edge constructor takes two vertices."""
        if len(vs) != 2:
            raise ValueError('Edges must connect exactly two vertices.')
        return tuple.__new__(cls, vs)

    def __repr__(self):
        """Return a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Edge({0}, {1})'.format(repr(self[0]), repr(self[1]))

    __str__ = __repr__
    """The str and repr forms of this object are the same."""


class Graph(dict):
    """
    A Graph is a dictionary of dictionaries.  The outer
    dictionary maps from a vertex to an inner dictionary.
    The inner dictionary maps from other vertices to edges.
    
    For vertices a and b, graph[a][b] maps
    to the edge that connects a->b, if it exists.
    """

    def __init__(self, vs=[], es=[]):
        """Creates a new graph.  
        vs: list of vertices;
        es: list of edges.
        """
        for v in vs:
            self.add_vertex(v)
            
        for e in es:
            self.add_edge(e)

    def add_vertex(self, v):
        """Add a vertex to the graph."""
        self[v] = {}

    def add_edge(self, e):
        """Adds and edge to the graph by adding an entry in both directions.

        If there is already an edge connecting these Vertices, the
        new edge replaces it.
        """
        v, w = e
        self[v][w] = e
        self[w][v] = e

    def get_edge(self, v1, v2):
        """Takes two vertices and returns the edge between them if it exists,
        None otherwise"""
        try:
            edge = self[v1][v2]
        except KeyError:
            edge = None
        return edge

    def remove_edge(self, e):
        """Takes an edge as its argument and deletes all references to that
        edge"""
        v1 = e[0]
        v2 = e[1]
        self[v1].pop(v2)
        self[v2].pop(v1)

    def vertices(self):
        """Return a list of all vertices in the graph"""
        return [vert for vert in self]

    def edges(self):
        "Return a list of all edges in the graph"
        res = []
        for vert in self:
            for vert2 in self[vert]:
                edge = self[vert][vert2]
                if not edge in res:
                    res.append(edge)
        return res

    def out_vertices(self, vert):
        """
        Takes a vertex as an argument and returns a list of the connected
        vertices
        """
        outs = [other for other in self[vert] if self.get_edge(vert, other)]
        return outs

    def out_edges(self, vert):
        """
        Takes a Vertex and returns a list of the connected edges
        """
        v2s = self.out_vertices(vert)
        all_edges = []
        for other in v2s:
            current = self.get_edge(vert, other)
            if current:
                all_edges.append(current)
            #print("All edges: ", all_edges)
        return all_edges

    def add_all_edges(self):
        """Starting with an edgeless graph, adds edges between each pair
        of vertices to form a complete graph.
        """
        for v1 in self.keys():
            for v2 in self.keys():
                if not v1 == v2:
                    new = Edge(v1, v2)
                    self.add_edge(new)
    def get_degree(self, vert):
        """Find the degree of the given vertex"""
        deg = len(self.out_vertices(vert))
        return deg

    def add_regular_edges(self, degree):
        """
        Starts with an edgeless graph, and adds edges so that every vertex
        has the same degree
        """
        regular = False
        all_vs = self.vertices()
        while not regular:
            checkv = random.choice(all_vs)
            other_vs = all_vs[:]
            other_vs.remove(checkv)
            if self.get_degree(checkv) < degree:
                for other in other_vs:
                    if self.get_degree(other) < degree:
                        new = Edge(checkv, other)
                        break
                self.add_edge(new)
            if self.check_regular(degree):
                regular = True

    def check_regular(self, degree):
        for v in self.vertices():
            if not len(self.out_vertices(v)) == degree:
                return False
        else:
            return True

            




def main(script, *args):
    v = Vertex('v')
    print(v)
    w = Vertex('w')
    print(w)
    e = Edge(v, w)
    print(e)
    g = Graph([v,w], [e])
    print(g)


if __name__ == '__main__':
#    import sys
#    main(*sys.argv)
#    print("Tests of new methods:\n")
#    v = Vertex('v')
#    w = Vertex('w')
#    x = Vertex('x')
#    e = Edge(v, w)
#    e2 = Edge(v, x)
#    g1 = Graph([v, w, x], [e, e2])
#    print("get_edge:")
#    print(g1.get_edge(v, w))
#    print("remove_edge: (should return None)")
#    print(g1.remove_edge(e2))
#    print("vertices")
#    print(g1.vertices())
#    print("edges")
#    print(g1.edges())
    print("Testing add_regular_edges:")
    chars = 'tuvwxyz'
    vertices = [Vertex(char) for char in chars]
    g = Graph(vertices, [])
    g.add_regular_edges(2)
