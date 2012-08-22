#! /usr/bin/env python3
import blessings


class RBTree:
    def __init__(self, vals, with_term=False):
        first = vals.pop(0)
        self.root = RBNode(NullNode(), first, 'B')
        for val in vals:
            self.add(self.root, val)
        if with_term:
            self.t = blessings.Terminal()

    def add(self, target_node, new_val):
        if new_val == target_node.value:
            print(new_val, " already exists")
            return
        if new_val < target_node.value:
            if not target_node.left:
                target_node.left = RBNode(target_node, new_val, 'R')
            else:
                self.add(target_node.left, new_val)
        elif new_val > target_node.value:
            if not target_node.right:
                target_node.right = RBNode(target_node, new_val, 'R')
            else:
                self.add(target_node.right, new_val)

    def term_print(self):
        print_col = {'R': self.t.red_on_white, 'B': self.t.black_on_white}
        print(print_col[self.root.colour](str(self.root.value)))
        print(print_col[self.root.left.colour](str(self.root.left.value)))


class RBNode:
    colours = ('R', 'B')

    def __init__(self, parent, value, colour):
        self.parent = parent
        self.value = value
        self.left = NullNode()
        self.right = NullNode()
        self.colour = colour

    def __bool__(self):
        return True

    def __str__(self):
        return str(self.value)


class NullNode(RBNode):
    def __init__(self):
        self.colour = 'B'
        self.value = 'Null'

    def __bool__(self):
        return False

if __name__ == '__main__':
    tree1 = RBTree([13, 17, 8, 11, 15, 1, 25, 6, 22, 27])
    print(tree1.root)
    tree2 = RBTree([13, 17, 8, 11, 15, 1, 25, 6, 22, 27], with_term=True)
    tree2.term_print()
