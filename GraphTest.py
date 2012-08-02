import Graph
import GraphWorld
import string

NODES = 10
DEGREE = 4
RANDOM_P = 0.1


def test_regular():
    test1 = string.ascii_lowercase[:NODES]
    vs1 = [Graph.Vertex(v) for v in test1]

    g1 = Graph.Graph(vs1, [])
    g1.add_regular_edges(DEGREE)
    lay1 = GraphWorld.CircleLayout(g1)

    gw = GraphWorld.GraphWorld()
    gw.show_graph(g1, lay1)
    gw.mainloop()


def test_random():
    import RandomGraph
    test1 = string.ascii_lowercase[:NODES]
    vs1 = [Graph.Vertex(v) for v in test1]

    g1 = RandomGraph.RandomGraph(vs1, [])
    g1.add_random_edges(RANDOM_P)
    lay1 = GraphWorld.CircleLayout(g1)

    gw = GraphWorld.GraphWorld()
    gw.show_graph(g1, lay1)
    gw.mainloop()

test_random()
