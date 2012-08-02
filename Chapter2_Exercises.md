Chapter 2 Exercises
===================

## Exercise 2.1
1. A **simple** graph is one in which each pair of vertices can only have one
edge connecting them, where there are no loops (edges starting and ending at
the same vertex), and which is *undirected*, i.e. connections between
vertices are two-way.

2. A **regular** graph is a graph where each vertex has the same number of 
neighbours. A **complete** graph is one where each vertex is connected to each
of the other vertices. All complete graphs are regular, since if there are
`N` vertices, each vertex will have `N - 1` neighbours.

3. A **path** is a sequence of vertices, where for each step in the sequence,
there is an edge connecting to two vertices. 
A **cycle** is a path where the start vertex is the same as the end vertex.

4. A **tree** is a **connected** graph that has only one simple path between
each pair of vertices, i.e.  there are no cycles, but there is a path from
every node to every other node. 

A **forest** also has no cycles, but it is not necessarily *connected*, i.e.
there is not necessarily a path between every point. Forests are therefore
composed entirely of (possibly connected) trees.
