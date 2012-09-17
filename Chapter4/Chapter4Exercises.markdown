Chapter 4 Exercises
===================

Exercise 4.2 
------------

The code provided in the book has a couple of performance errors:

* To get the current node, the code uses `queue.pop(0)`, which is
**O(n)**. `queue.pop()`, without an argument, does the same
thing and is **O(1)**. Alternatively, a FIFO data structure like
`collections.deque` always has **O(1)** for `pop`, so you're less likely
to accidentally run into the **O(n)** issue.
* Not sure what the other error is?

Exercise 4.3
------------

1. Watts and Strogatz rewire their graphs by choosing a probability, *p*. For
each edge of the graph, there is a random/draw roll, and if the draw falls
within *p*, one end of the edge is reassigned to a random vertex within 
the graph (disallowing duplicate edges)

2. *C(p)* is defined as the average of *Cv* for all *v* in the graph, where
*Cv* is the proportion of neighbours that *v* could be connected to, i.e. the 
number of neighbours divided by *kv(kv - 1)*.

3. The average path length, *Lv*, is defined as the average number of links
in the shortest path connecting any two nodes.

4. Watts and Strogatz looked at actors who had appeared in a movie together,
the electrical grid of the Western United States, and the neural network
of the worm *C. elegans*. These graphs had the same structure as their model
because the path lengths were short, like a random graph, but the clustering
coefficiens were high, like a regular graph.

