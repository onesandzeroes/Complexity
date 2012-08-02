import Graph
import GraphWorld
import string

NODES = 14
DEGREE = 2

test1 = string.ascii_lowercase[:NODES]
vs1 = [Graph.Vertex(v) for v in test1]

g1 = Graph.Graph(vs1, [])
g1.add_regular_edges(DEGREE)
lay1 = GraphWorld.CircleLayout(g1)

gw = GraphWorld.GraphWorld()
gw.show_graph(g1, lay1)
gw.mainloop()
