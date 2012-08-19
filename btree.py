class BTree:
    def __init__(self, items=None):
        if items is None:
            self.items = []
        else:
            self.items = items
        self.root = None
        self.build()

    def build(self):
        if self.root is None:
            self.root = TreeItem(self.items.pop(0))
        for item in self.items:
            self.root.add(item)

    def __str__(self):
        spacing = 80
        final_string = ''
        next_layer = [self.root]
        while True:
            current_layer = next_layer
            nones = [node for node in current_layer if node is None]
            # If all in current_layer are None
            if len(current_layer) == len(nones):
                break
            for node in current_layer:
                final_string += str(node).center(spacing)
            final_string += '\n'
            next_layer = []
            for node in current_layer:
                if not node is None:
                    next_layer.append(node.left)
                    next_layer.append(node.right)
                else:
                    next_layer.append(None)
                    next_layer.append(None)
            spacing = spacing // 2
        return final_string


class TreeItem:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def add(self, val):
        if val < self.val:
            if self.left is None:
                self.left = TreeItem(val)
            else:
                self.left.add(val)
        elif val > self.val:
            if self.right is None:
                self.right = TreeItem(val)
            else:
                self.right.add(val)

    def __str__(self):
        return str(self.val)

if __name__ == '__main__':
    btree = BTree([8, 10, 3, 1, 6, 14, 4, 7, 13])
    print(btree)
