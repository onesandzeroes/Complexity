#! /usr/bin/env python3
"""
Re-implementing a hashtable data structure like a Python dict
"""

class LinearMap:
    def __init__(self):
        self.items = []

    def add(self, k, v):
        """
        Add a new item that maps from key k to value v
        """
        self.items.append((k, v))

    def get(self, k):
        """
        Look up and return the value that corresponds to k
        """
        for key, val in self.items:
            if key == k:
                return val
        raise KeyError
