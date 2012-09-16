#! /usr/bin/env python3
from Graph import Vertex
from RandomGraph import RandomGraph
import collections
import string
import os
import matplotlib.pyplot as pyplot


# Dummy visit function, to pass to the bfs functions when testing
def dummy_visit(node):
    pass


def bfs_orig(top_node, visit, graph):
    """
    Breadth-first serach on a graph, starting at top node
    """
    visited = set()
    queue = [top_node]
    while len(queue):
        curr_node = queue.pop(0)
        visit(curr_node)
        visited.add(curr_node)
        # Enqueue non-visited/non-queued children
        queue.extend(c for c in graph.out_vertices(curr_node)
                     if c not in visited and c not in queue)


# Found a site that said that for Python lists, pop(0) was O(n) while
# just pop() was O(1), but that doesn't seem to be the case, this function
# has the same time complexity as the original
def bfs_fixpop(top_node, visit, graph):
    """
    Use pop() instead of pop(0)
    """
    visited = set()
    queue = [top_node]
    while len(queue):
        curr_node = queue.pop()
        visit(curr_node)
        visited.add(curr_node)
        # Enqueue non-visited/non-queued children
        queue.extend(c for c in graph.out_vertices(curr_node)
                     if c not in visited and c not in queue)


def bfs_deque(top_node, visit, graph):
    """
    Use collections.deque for the queue, as its pop() method
    should be O(1)
    """
    visited = set()
    queue = collections.deque([top_node])
    while len(queue):
        curr_node = queue.popleft()
        visit(curr_node)
        visited.add(curr_node)
        # Enqueue non-visited/non-queued children
        for c in graph.out_vertices(curr_node):
            if c not in visited:
                if c not in queue:
                    queue.append(c)


def gen_alphanum():
    while True:
        for n in string.digits:
            for c in string.lowercase:
                yield c + str(n)


def etime():
    """see how much user and system time this process has used
    so far and return the sum"""
    user, sys, chuser, chsys, real = os.times()
    return user + sys


def test_bfs(bfs_func, maxpow):
    ns = []
    ts = []
    max_n = 8 * (10 ** maxpow)
    for n in range(5, max_n, 10):
        ns.append(n)
        nodes = []
        for each in range(n):
            nodes.append(Vertex(gen_alphanum()))
        g = RandomGraph(vs=nodes)
        g.add_random_edges(0.3)
        search_vertex = g.vertices()[0]
        # Actual BFS starts here
        start = etime()
        bfs_func(search_vertex, dummy_visit, g)
        end = etime()
        # ANd ends here
        search_time = end - start
        ts.append(search_time)
    return {'sizes': ns, 'times': ts}


def graph_results(title, res_dict):
    """
    Takes a results dictionary from the test_bfs function
    and graphs those results
    """
    pyplot.plot(res_dict['sizes'], res_dict['times'])
    pyplot.title(title)
    pyplot.xlabel('n')
    pyplot.ylabel('t')
    pyplot.show()


def compare_funcs(title, func1, func2, maxpow=2):
    r1 = test_bfs(func1, maxpow)
    r2 = test_bfs(func2, maxpow)
    pyplot.plot(
        r1['sizes'], r1['times'], 'ro',
        r2['sizes'], r2['times'], 'bs',
    )
    pyplot.title(title)
    pyplot.xlabel('n')
    pyplot.ylabel('t')
    pyplot.show()


if __name__ == '__main__':
    # This works fine but takes ages, so I won't run it every time
    # compare_funcs("Original (red) vs Fixed pop() (blue)",
    #               bfs_orig, bfs_fixpop, 2)
    compare_funcs("Original (red) vs Using deque() (blue)",
                  bfs_orig, bfs_deque, 2)
