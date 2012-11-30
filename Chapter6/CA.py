""" Code example from Complexity and Computation, a book about
exploring complexity science with Python.  Available free from

http://greenteapress.com/complexity

Copyright 2011 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
"""

import numpy


class CA:
    """A CA is a cellular automaton; the parameters for __init__ are:

    rule:  an integer in the range 0-255 that represents the CA rule
           using Wolfram's encoding.
    n:     the number of rows (timesteps) in the result.
    ratio: the ratio of columns to rows.
    """

    def __init__(self, rule, n=100, ratio=2):
        """Attributes:
        table:  rule dictionary that maps from triple to next state.
        n, m:   are the number of rows, columns.
        array:  the numpy array that contains the data.
        next:   the index of the next empty row.
        """
        self.table = self.make_table(rule)
        self.n = n
        self.m = ratio * n + 1
        self.array = numpy.zeros((n, self.m), dtype=numpy.int8)
        self.next = 0

    def make_table(self, rule):
        """Returns a table for the given CA rule.  The table is a
        dictionary that maps 3-tuples to binary values.
        """
        table = {}
        for i, bit in enumerate(binary(rule, 8)):
            t = binary(7 - i, 3)
            table[t] = bit
        return table

    def start_single(self):
        """Starts with one cell in the middle of the top row."""
        self.array[0, self.m // 2] = 1
        self.next += 1

    def start_random(self):
        """Start with random values in the top row."""
        self.array[0] = numpy.random.random([1, self.m]).round()
        self.next += 1

    def loop(self, steps=1):
        """Executes the given number of time steps."""
        [self.step() for i in range(steps)]

    def step(self):
        """Executes one time step by computing the next row of the array."""
        i = self.next
        self.next += 1

        a = self.array
        t = self.table
        for j in range(1, self.m - 1):
            a[i, j] = t[tuple(a[i - 1, j - 1:j + 2])]

    def get_array(self, start=0, end=None):
        """Gets a slice of columns from the CA, with slice indices
        (start, end).  Avoid copying if possible.
        """
        if start == 0 and end is None:
            return self.array
        else:
            return self.array[:, start:end]


class CircularCA(CA):
    """
    A "ring-shaped" version of the CA where
    the ends wrap-around
    """

    def __init__(self, rule, n=100, ratio=2):
        self.table = self.make_table(rule)
        self.n = n
        self.m = ratio * n + 2 + 1
        self.array = numpy.zeros((n, self.m), dtype=numpy.int8)
        self.next = 0

    def start_single(self):
        """
        Start with a cell in the left of the first row,
        instead of in the middle
        """
        self.array[0, 1] = 1
        self.next += 1

    def step(self):
        i = self.next
        self.next += 1

        a = self.array
        t = self.table
        # Copy actual end points into the
        # ghost cells to produce the wraparound
        a[i - 1, 0] = a[i - 1, self.m - 2]
        a[i - 1, self.m - 1] = a[i - 1, 1]
        for j in range(1, self.m - 1):
            a[i, j] = t[tuple(a[i - 1, (j - 1):(j + 2)])]

    def get_array(self, start=0, end=None):
        """
        Get a slice of columns from the CA,
        clipping off the ghost cells at either end of
        the row.
        """
        if end is None:
            return self.array[:, (start + 1):(self.m - 1)]
        else:
            return self.array[:, (start + 1):(end + 1)]


def binary(n, digits):
    """Returns a tuple of (digits) integers representing the
    integer (n) in binary.  For example, binary(3,3) returns (0, 1, 1)"""
    t = []
    for i in range(digits):
        n, r = divmod(n, 2)
        t.append(r)

    return tuple(reversed(t))


def print_table(table):
    """Prints the rule table in LaTeX format."""
    t = list(table.items())
    t.sort(reverse=True)

    print('\\beforefig')
    print('\\centerline{')
    print('\\begin{tabular}{|c|c|c|c|c|c|c|c|c|}')
    print('\\hline')

    res = ['prev']
    for k, v in t:
        s = ''.join([str(x) for x in k])
        res.append(s)
    print(' & '.join(res) + ' \\\\ \n\\hline')

    res = ['next']
    for k, v in t:
        res.append(str(v))
    print(' &   '.join(res) + ' \\\\ \n\\hline')

    print('\\end{tabular}}')
