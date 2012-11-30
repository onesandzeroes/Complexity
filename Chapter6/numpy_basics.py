#! /usr/bin/env python3
import numpy


class CA:

    def __init__(self, rule, n=100, ratio=2):
        self.table = make_table(rule)
        self.n = n
        self.m = ratio * n + 1
        self.array = numpy.zeros((n, self.m), dtype=numpy.int8)
        self.next = 0

    def start_single(self):
        """
        Starts with one cell in the middle of the top row
        """
        self.array[0, self.m // 2] = 1
        self.next += 1

    def step(self):
        i = self.next
        self.next += 1

        a = self.array
        t = self.table
        for j in range(1, self.m - 1):
            a[i, j] = t[tuple(a[(i - 1), (j - 1):(j + 2)])]


class Drawer:
    """
    Drawer is an abstract class that should not be instantiated.
    It defines the interface for a CA drawer; child classes of Drawer
    should implement draw, show and save.

    If draw_array is not overridden, the child class should provide
    draw_cell.
    """
    def __init__(self):
        msg = "Drawer is an abstract type and should no be instantiated"
        raise NotImplementedError(msg)

    def draw(self, ca):
        """
        Draws a representation of cellular automaton (CA).
        This function generally has no visible effect.
        """
        raise NotImplementedError

    def draw_array(self, a):
        """
        Iterate through array (a) and draws any non-zero cells.
        """
        for i in range(self.rows):
            for j in range(self.cols):
                if a[i, j]:
                    self.draw_cell(j, self.rows - i - 1)

    def draw_cell(self, ca):
        """
        Draws a single cell.
        Not required for all implementations.
        """
        raise NotImplementedError

    def show(self):
        """
        Displays a representation on the screen, if possible.
        """
        raise NotImplementedError

    def save(self, filename):
        """
        Saves the representation of the CA in filename.
        """
        raise NotImplementedError

