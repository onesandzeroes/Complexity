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

class BetterMap:
    def __init__(self, n=100):
        self.maps = []
        for i in range(n):
            self.map.append(LinearMap())

    def find_map(self, k):
        index = hash(k) % len(self.maps)
        return self.maps[index]

    def add(self, k, v):
        m = self.find_map(k)
        m.add(k, v)

    def get(self, k):
        m = self.find_map(k)
        return m.get(k)

class HashMap:
    def __init__(self):
        self.maps = BetterMap(2)
        self.num = 0

    def get(self, k):
        return self.maps.get(k)

    def add(self, k, v):
        if self.num == len(self.maps.maps):
            self.resize()
        self.maps.add(k, v)
        self.num += 1

    def resize(self):
        new_maps = BetterMap(self.num * 2)
        for m in self.maps.maps:
            for k, v in m.items:
                new_maps.add(k, v)
