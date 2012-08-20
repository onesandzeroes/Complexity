#! /usr/bin/env python3
import blessings


class RBTree:
    def __init__(self, vals, with_term=False):
        first = vals.pop(0)
        self.root = RBNode(first, 'B')
        for val in vals:
            self.root.add(val)
        if with_term:
            self.t = blessings.Terminal()

    def term_print(self):
        print_col = {'R': self.t.red_on_white, 'B': self.t.black_on_white}
        print(print_col[self.root.colour](str(self.root.value)))
        print(print_col[self.root.left.colour](str(self.root.left.value)))


class RBNode:
    colours = ('R', 'B')

    def __init__(self, value, colour):
        self.value = value
        self.left = NullNode()
        self.right = NullNode()
        self.colour = colour

    def __bool__(self):
        return True

    def add(self, new_val):
        if self.colour == 'R':
            child_colour = 'B'
        elif self.colour == 'B':
            child_colour = 'R'
        if new_val < self.value:
            if not self.left:
                self.left = RBNode(new_val, child_colour)
            else:
                self.left.add(new_val)
        elif new_val > self.value:
            if not self.right:
                self.right = RBNode(new_val, child_colour)
            else:
                self.right.add(new_val)

    def __str__(self):
        return str(self.value)


class NullNode:
    def __init__(self):
        self.colour = 'B'

    def __bool__(self):
        return False

    def __str__(self):
        return 'Null'

if __name__ == '__main__':
    tree1 = RBTree([13, 17, 8, 11, 15, 1, 25, 6, 22, 27])
    print(tree1.root)
    tree2 = RBTree([13, 17, 8, 11, 15, 1, 25, 6, 22, 27], with_term=True)
    tree2.term_print()