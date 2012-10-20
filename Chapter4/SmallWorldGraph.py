#! /usr/bin/env python3
import random
import collections
import itertools
import os
import matplotlib.pyplot as pyplot
import networkx as nx


def etime():
    """see how much user and system time this process has used
    so far and return the sum"""
    user, sys, chuser, chsys, real = os.times()
    return user + sys


class SmallWorldGraph(nx.Graph):
    def __init__(self, n, k, p):
        nx.Graph.__init__(self)
        create = nx.watts_strogatz_graph(n, k, p)
        self.add_nodes_from(create.nodes())
        self.add_edges_from(create.edges())
        self.known_paths = {}

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
        if max_connects == 0:
            return 0
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

    def shortest_paths(self, source_node):
        res_dict = {node: None for node in self.nodes()}
        res_dict[source_node] = 0
        queue = collections.deque([source_node])
        while queue:
            current_node = queue.popleft()
            d = res_dict[current_node]
            for n in self.neighbors(current_node):
                if res_dict[n] is None:
                    queue.append(n)
                    res_dict[n] = d + 1
                elif res_dict[n] > d + 1:
                    res_dict[n] = d + 1
        final = {(source_node, n): res_dict[n] for n in res_dict}
        return final

    def shortest_path_average(self):
        paths = {}
        for node in self.nodes():
            new_paths = self.shortest_paths(node)
            for p in new_paths:
                opp = (p[1], p[0])
                if not opp in paths:
                    paths[p] = new_paths[p]
        dists = []
        for p in paths:
            if not paths[p] is None:
                dists.append(paths[p])
        return sum(dists) / len(dists)

    def shortest_path_all_pairs(self, check_time=False):
        if check_time:
            print("Finding paths: ")
        n = len(self)  # len() of a Graph is the number of nodes
        distance = {0: {}}
        for i in self.nodes():
            distance[0][i] = {}
            for j in self.nodes():
                if not i == j:
                    if self.has_edge(i, j):
                        distance[0][i][j] = 1  # Weights would go here
                    else:
                        distance[0][i][j] = float("inf")
                else:
                    distance[0][i][j] = 0
        for k in range(1, n + 1):
            k_node = self.nodes()[k - 1]
            distance[k] = {}
            for i in self.nodes():
                distance[k][i] = {}
                for j in self.nodes():
                    in_k = distance[k - 1][i][j]
                    i_to_k = distance[k - 1][i][k_node]
                    k_to_j = distance[k - 1][k_node][j]
                    outside_k = i_to_k + k_to_j
                    distance[k][i][j] = min(in_k, outside_k)
        if check_time:
            print("Finalizing results: ")
        all_pairs = itertools.combinations(self.nodes(), 2)
        final_dists = {pair: float("inf") for pair in all_pairs}
        for pair in final_dists:
            for k in distance:
                current_dist = distance[k][pair[0]][pair[1]]
                if current_dist < final_dists[pair]:
                    final_dists[pair] = current_dist
        return final_dists


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


def graph_c(n, k, iterations=20):
    ps = []
    cs = []
    for i in range(1, 10):
        ps.extend((10 ** power) * i for power in range(-4, 0))
    for p in ps:
        c0s = []
        cps = []
        for it in range(iterations):
            g = SmallWorldGraph(n, k, 0)
            c0 = g.clustering_coefficient()
            c0s.append(c0)
            g.rewire(p)
            cp = g.clustering_coefficient()
            cps.append(cp)
        c0_average = sum(c0s) / len(c0s)
        cp_average = sum(cps) / len(cps)
        cs.append(cp_average / c0_average)
    pyplot.plot(ps, cs, 'ws')
    pyplot.xscale('log')
    pyplot.show()


def graph_l(n, k, iterations=20):
    ps = []
    ls = []
    for i in range(1, 10):
        ps.extend((10 ** power) * i for power in range(-4, 0))
    for p in ps:
        l0s = []
        lps = []
        for it in range(iterations):
            g = SmallWorldGraph(n, k, 0)
            l0 = g.shortest_path_average()
            l0s.append(l0)
            g.rewire(p)
            lp = g.shortest_path_average()
            lps.append(lp)
        l0_average = sum(l0s) / len(l0s)
        lp_average = sum(lps) / len(lps)
        ls.append(lp_average / l0_average)
    pyplot.plot(ps, ls, 'ko')  # In matplotlib, 'k' = black
    pyplot.xscale('log')
    pyplot.show()


def graph_c_and_l(n, k, iterations=20):
    ps = []
    cs = []
    ls = []
    for i in range(1, 10):
        ps.extend((10 ** power) * i for power in range(-4, 0))
    for p in ps:
        c0s = []
        cps = []
        l0s = []
        lps = []
        for it in range(iterations):
            g = SmallWorldGraph(n, k, 0)
            c0 = g.clustering_coefficient()
            l0 = g.shortest_path_average()
            c0s.append(c0)
            l0s.append(l0)
            g.rewire(p)
            cp = g.clustering_coefficient()
            cps.append(cp)
            lp = g.shortest_path_average()
            lps.append(lp)
        c0_average = sum(c0s) / len(c0s)
        cp_average = sum(cps) / len(cps)
        cs.append(cp_average / c0_average)
        l0_average = sum(l0s) / len(l0s)
        lp_average = sum(lps) / len(lps)
        ls.append(lp_average / l0_average)
    pyplot.plot(ps, cs, 'ws', ps, ls, 'ko')
    pyplot.xscale('log')
    pyplot.savefig('watts-small_world_graph.svg')


def test_shortest_path(iterations=20):
    fails = 0
    for i in range(iterations):
        g = SmallWorldGraph(20, 4, 0.5)
        my_res = g.shortest_paths(0)[(0, 11)]
        nx_res = nx.shortest_path_length(g, 0, 11)
        if not my_res == nx_res:
            print("My result: {0}, nx {1}".format(my_res, nx_res))
            fails += 1
    if fails == 0:
        print("Passed!")
    else:
        print("Failed!")


def test_shortest_path_all_pairs(iterations=20):
    for i in range(iterations):
        g = SmallWorldGraph(20, 4, 0.5)
        print("Finding my results: ")
        my_results = g.shortest_path_all_pairs()
        print("Finding nx results: ")
        nx_results = nx.floyd_warshall(g)
        for key in my_results:
            my_res = my_results[key]
            nx_res = nx_results[key[0]][key[1]]
            if not my_res == nx_res:
                print("Mismatch!")


def complexity_all_pairs(max_size, iterations=10):
    size = []
    time = []
    for n in range(10, max_size, 10):
        nodes = n
        size.append(nodes)
        g = SmallWorldGraph(nodes, 4, 0.5)
        start = etime()
        # Iterate to get a stable estimate of the time
        for it in range(iterations):
            g.shortest_path_all_pairs()
        end = etime()
        time.append(end - start)
    fitted_times = fit(size, time, exp=3)
    print(fitted_times)
    print("Sizes: ", size)
    print("Times: ", time)
    pyplot.plot(size, time, 'bo')
    pyplot.plot(size, fitted_times)
    pyplot.title("Complexity of Floyd-Warshall")
    pyplot.savefig("shortest_path_complexity.png")


def compare_complexity(max_size, iterations=10):
    size = []
    d_time = []
    f_time = []
    for n in range(10, max_size, 10):
        nodes = n
        size.append(nodes)
        g = SmallWorldGraph(nodes, 4, 0.5)
        # Get Dijkstra time:
        start = etime()
        # Iterate to get a stable estimate of the time
        for it in range(iterations):
            nx.all_pairs_dijkstra_path_length(g)
        end = etime()
        d_time.append(end - start)
        # Get Floyd-Warshall time
        start = etime()
        # Iterate to get a stable estimate of the time
        for it in range(iterations):
            g.shortest_path_all_pairs()
        end = etime()
        f_time.append(end - start)
    pyplot.plot(size, d_time, 'rs')
    pyplot.plot(size, f_time, 'bo')
    pyplot.title("Floyd-Warshall (blue) vs Dijkstra (red)")
    pyplot.savefig("shortest_path_compare.png")


def fit(ns, ts, exp=1.0, index=-1):
    """Fits a curve with the given exponent.

    Use the given index as a reference point, and scale all other
    points accordingly.
    """
    nref = ns[index]
    tref = ts[index]

    tfit = []
    for n in ns:
        ratio = float(n) / nref
        t = ratio ** exp * tref
        tfit.append(t)
    return tfit

if __name__ == '__main__':
    compare_complexity(max_size=100)

    # complexity_all_pairs(max_size=120)

    # g = SmallWorldGraph(10, 2, 0.5)
    # print(g.shortest_path_all_pairs())
    #test_shortest_path_all_pairs(iterations=1)

    # graph_c_and_l(1000, 10)

    # graph_l(20, 4)

    # test_shortest_path()

    # g = SmallWorldGraph(20, 4, 0.5)
    # print(g.shortest_path(0, 11))
    # print(nx.shortest_path_length(g, 0, 11))
    # nx.draw_random(g)
    # pyplot.show()

    # This mimics the graph in the Watts Small World paper
    # graph_c(1000, 10)

    # g = SmallWorldGraph(500, 20, 0)
    # test_node = g.nodes()[0]
    # print(g.clustering_coefficient_node(test_node))
    # print(nx.clustering(g, test_node))
    # print(g.clustering_coefficient())
    # print(nx.average_clustering(g))
    # g.rewire(0.5)
    # print(g.clustering_coefficient_node(test_node))
    # print(nx.clustering(g, test_node))
    # print(g.clustering_coefficient())
    # print(nx.average_clustering(g))
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
