import random
import matplotlib.pyplot as pyplot
import networkx
import Cdf


def barabasi_gen(start_size, total_size, m):
    """
    Generate a graph according to the process outlined in Barabasi
    and Albert, where vertices are added one at a time, and attach to
    existing vertices with probability:
        p(existing) = deg(existing) / sum(deg(all_vertices))
    """
    if m > start_size:
        print("m must be >= than the initial number of vertices")
        return None
    # Start with an Erdos-Renyi random graph?
    g = networkx.gnp_random_graph(start_size, p=(m / start_size))
    # Need to number each node, so start with:
    new_node = start_size + 1
    while len(g) < total_size:
        # Create the list of other nodes before adding the new node,
        # easiest way to do it
        others = g.nodes()
        # Calculate the probabilities every time, or find a cleverer
        # way of updating the values?
        total_degree = sum(deg for node, deg in g.degree_iter())
        g.add_node(new_node)
        while g.degree(new_node) < m:
            node_to_check = random.choice(others)
            prob = g.degree(node_to_check) / total_degree
            dice_roll = random.random()
            if dice_roll < prob:
                g.add_edge(new_node, node_to_check)
        new_node += 1
    return g


def graph_pk(graph, title):
    graph_degs = [deg for node, deg in graph.degree_iter()]
    deg_cdf = Cdf.MakeCdfFromList(graph_degs)
    degs, probs = deg_cdf.Render()
    ccdf = [(1 - p) for p in probs]
    pyplot.plot(degs, ccdf, 'ro')
    pyplot.xscale('log', basex=10)
    pyplot.yscale('log', basey=10)
    pyplot.title(title)
    pyplot.savefig('barabasi_albert_sim.png', format='png')


def test_clustering(size):
    print("Barabasi-Albert:")
    ba = networkx.barabasi_albert_graph(1000, 4)
    print("Clustering: ", networkx.average_clustering(ba))
    print("Average length: ", networkx.average_shortest_path_length(ba))
    print("Watts-Strogatz:")
    ws = networkx.watts_strogatz_graph(size, 4, 0.001)
    print("Clustering: ", networkx.average_clustering(ws))
    print("Average length: ", networkx.average_shortest_path_length(ws))


if __name__ == '__main__':
    test_clustering(1000)

    # g = barabasi_gen(5, 1000, 5)
    # graph_pk(g, 'Barbasi-Albert Network')
