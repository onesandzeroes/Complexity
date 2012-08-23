#! /usr/bin/env python3
import blessings


class RBTree:
    def __init__(self, vals):
        first = vals.pop(0)
        # Create root node with no parent
        self.root = RBNode(None, first, 'B', self)
        for val in vals:
            self.root.add(val)

    def add(self, target_node, new_val):
        if new_val == target_node.value:
            print(new_val, " already exists")
            return
        if new_val < target_node.value:
            if not target_node.left:
                target_node.left = RBNode(target_node, new_val, 'R', self)
                # Check if the tree needs to be adjusted after insertion
                target_node.left.property_check()
            else:
                self.add(target_node.left, new_val)
        elif new_val > target_node.value:
            if not target_node.right:
                target_node.right = RBNode(target_node, new_val, 'R', self)
                target_node.right.property_check()
            else:
                self.add(target_node.right, new_val)

    def colour_print(self):
        t = blessings.Terminal()
        print_col = {'R': t.red_on_black, 'B': t.white_on_black}
        node = self.root
        val, col = node.colour_str()
        out = print_col[col](val)
        print(out)

    def rotate(self, node, direction):
        print("Rotating ", direction)
        if node == self.root:
            reroot_tree = True
        else:
            reroot_tree = False
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

    def __init__(self, parent, value, colour, tree):
        self.parent = parent
        self.value = value
        self.colour = colour
        self.tree = tree
        self.left = NullNode(parent=self, tree=tree)
        self.right = NullNode(parent=self, tree=tree)

    def __bool__(self):
        return True

    def __str__(self):
        return str(self.value)

    def add(self, new_val):
        if new_val == self.value:
            print(new_val, " already exists")
            return
        if new_val < self.value:
            if not self.left:
                self.left = RBNode(self, new_val, 'R', self)
                # Check if the tree needs to be adjusted after insertion
                self.left.property_check()
            else:
                self.left.add(new_val)
        elif new_val > self.value:
            if not self.right:
                self.right = RBNode(self, new_val, 'R', self)
                self.right.property_check()
            else:
                self.right.add(new_val)

    def get_grandparent(self):
        if self.parent:
            if self.parent.parent:
                return self.parent.parent
        # return None if either test fails
        return None

    def get_uncle(self):
        g = self.get_grandparent()
        if g:
            if self.parent == g.left:
                return g.right
            elif self.parent == g.right:
                return g.left
        else:
            return None

    def property_check(self):
        """
        Checks that the properties of red-black trees still hold, and fixes
        the tree if necessary. Should be called after an add/remove operation
        """
        # If node has no parent, shouldn't actually happen since
        # the root is created separately
        if not self.parent:
            self.colour = 'B'
            return
        # If the parent is black, fine, since both children of a black
        # node are red
        if self.parent.colour == 'B':
            self.colour = 'R'
            return
        # Next few tests assume a grandparent
        g = self.get_grandparent()
        if not g:
            return
        # If both the parent and the uncle are red:
        uncle = self.get_uncle()
        if uncle and uncle.colour == 'R':
            self.parent.colour = 'B'
            uncle.colour = 'B'
            g.colour = 'R'
            # Recursive property check
            g.property_check()
            # Need to end here
            return
        # If parent is red but uncle is black, and self is the right
        # chlid of parent, rotate parent left
        if self == self.parent.right and self.parent == g.left:
            self.tree.rotate(self.parent, 'left')
            self = self.left
        # And same in the other direction
        elif self == self.parent.left and self.parent == g.right:
            self.tree.rotate(self.parent, 'right')
            self = self.right
        # If parent is red, uncle is black, self is the left child
        # of parent, and parent is the left child of g:
        self.parent.colour = 'B'
        g.colour = 'R'
        if self == self.parent.left:
            self.tree.rotate(g, 'right')
        else:
            self.tree.rotate(g, 'left')

    def colour_str(self):
        """
        Return a tuple containing the value and colour of the node,
        to allow for pretty printing of the tree
        """
        return (str(self.value), self.colour)


class NullNode(RBNode):
    def __init__(self, parent, tree):
        self.colour = 'B'
        self.value = 'Null'

    def __bool__(self):
        return False

if __name__ == '__main__':
    tree1 = RBTree([13, 17, 8, 11, 15, 1, 25, 6, 22, 27])
    print(tree1.root)
    tree2 = RBTree([13, 17, 8, 11, 15, 1, 25, 6, 22, 27])
    tree2.colour_print()
    tree2.root.colour = 'B'
    tree2.colour_print()
    print("Testing rotate:")
    tree3 = RBTree([5, 3, 7, 2, 4])
    print("Before rotation, root: ", tree3.root, "root.left: ",
          tree3.root.left, "root.right: ", tree3.root.right)
    tree3.rotate(tree3.root, 'right')
    print("After rotation, root: ", tree3.root, "root.left: ",
          tree3.root.left, "root.right: ", tree3.root.right)
