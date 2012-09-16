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

