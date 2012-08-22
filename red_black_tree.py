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
                # Check if the tree needs to be adjusted after insertion
                target_node.left.property_check()
        elif new_val > target_node.value:
            if not target_node.right:
                target_node.right = RBNode(target_node, new_val, 'R')
            else:
                self.add(target_node.right, new_val)
                target_node.right.property_check()

    def term_print(self):
        print_col = {'R': self.t.red_on_white, 'B': self.t.black_on_white}
        print(print_col[self.root.colour](str(self.root.value)))
        print(print_col[self.root.left.colour](str(self.root.left.value)))

    def rotate(self, node, direction):
        if node == self.root:
            reroot_tree = True
        if direction.lower() in ('l', 'left'):
            pivot = node.right
            node.right = pivot.left
            pivot.left = node
            node = pivot
        elif direction.lower() in ('r', 'right'):
            pivot = node.left
            node.left = pivot.right
            pivot.right = node
            node = pivot
        if reroot_tree:
            self.root = node


class RBNode:
    colours = ('R', 'B')

    def __init__(self, parent, value, colour):
        self.parent = parent
        self.value = value
        self.left = NullNode(self)
        self.right = NullNode(self)
        self.colour = colour

    def __bool__(self):
        return True

    def __str__(self):
        return str(self.value)

    def get_grandparent(self):
        if self.parent:
            if self.parent.parent:
                return self.parent.parent
        # return None if either test fails
        return None

    def get_uncle(self):
        gp = self.get_grandparent()
        if gp:
            if self.parent == gp.left:
                return gp.right
            elif self.parent == gp.right:
                return gp.left
        return None

    def property_check(self):
        # If node has no parent, shouldn't actually happen since
        # the root is created separately
        if not self.parent:
            self.colour = 'B'
            return
        # If the parent is black, fine, since both children of a black
        # node are red
        if self.parent.colour == 'B':
            return
        # If both the parent and the uncle are red:
        uncle = self.get_uncle()
        if uncle and uncle.colour == 'R':
            self.parent.colour = 'B'
            uncle.colour = 'B'
            g = self.get_grandparent()
            g.colour = 'R'
            # Recursive property check
            g.property_check()


class NullNode(RBNode):
    def __init__(self, parent=None):
        self.colour = 'B'
        self.value = 'Null'

    def __bool__(self):
        return False

if __name__ == '__main__':
    tree1 = RBTree([13, 17, 8, 11, 15, 1, 25, 6, 22, 27])
    print(tree1.root)
    tree2 = RBTree([13, 17, 8, 11, 15, 1, 25, 6, 22, 27], with_term=True)
    tree2.term_print()
    print("Testing rotate:")
    tree3 = RBTree([5, 3, 7, 2, 4])
    print("Before rotation, root: ", tree3.root, "root.left: ",
          tree3.root.left, "root.right: ", tree3.root.right)
    tree3.rotate(tree3.root, 'right')
    print("After rotation, root: ", tree3.root, "root.left: ",
          tree3.root.left, "root.right: ", tree3.root.right)
