#! /usr/bin/env python3


class DoubleNode:
    def __init__(self, val, prev=None, after=None):
        self.val = val
        self.prev = prev
        self.after = after

    def __bool__(self):
        """
        Return True if the value of the node is True
        """
        return bool(self.val)

    def __str__(self):
        return str(self.val)


class DoubleList:
    def __init__(self, data):
        self.first = DoubleNode(data[0])
        self.last = self.first
        for v in data[1:]:
            self.append(v)

    def append(self, val):
        """
        Add a value to the end of the list
        """
        self.last.after = DoubleNode(val, prev=self.last)
        self.last = self.last.after

    def pop(self):
        """
        Remove and return the item at the front of the list
        """
        popped = self.first.val
        self.first = self.first.after
        self.first.prev = DoubleNode(None, after=self.first)
        return(popped)


if __name__ == '__main__':
    test = DoubleList([12, 99, 37])
    print("First: ", test.first, "Last: ", test.last)
    print(test.pop())
    print("First: ", test.first, "Last: ", test.last)
