import os
import matplotlib.pyplot as pyplot
from hashtables import LinearMap, BetterMap, HashMap
import random


def etime():
    """see how much user and system time this process has used
    so far and return the sum"""
    user, sys, chuser, chsys, real = os.times()
    return user + sys


def test_map(name, num_keys, num_tests=50):
    """
    Takes the name of a map implementation as a string,
    and a size, in terms of number of keys, and returns
    the mean time taken to get a random key
    """
    map_func = eval(name)
    m = map_func()
    all_keys = list(range(num_keys))
    for k in all_keys:
        m.add(k, 'a')
    times = []
    for n in range(num_tests):
        lookup = random.choice(all_keys)
        start = etime()
        m.get(lookup)
        end = etime()
        t = end - start
        times.append(t)
    average = sum(times) / len(times)
    return average


def test_range(name, pow1, pow2):
    ns = []
    ts = []
    for p in range(pow1, pow2):
        for i in (1, 2, 4, 8):
            num_keys = (10 ** p) * i
            t = test_map(name, num_keys)
            ns.append(num_keys)
            ts.append(t)
    return {'ns': ns, 'ts': ts}


def make_fig(name, pow1, pow2,  scale='log'):
    pyplot.clf()
    pyplot.xscale(scale)
    pyplot.yscale(scale)
    pyplot.title(name)
    pyplot.xlabel('n')
    pyplot.ylabel('run time (s)')
    data = test_range(name, pow1, pow2)
    pyplot.plot(data['ns'], data['ts'], linewidth=3)
    pyplot.show()


def plot(ns, ts, label, color='blue', exp=1.0):
    pyplot.plot(ns, ts, label=label, color=color, linewidth=3)

if __name__ == '__main__':
    make_fig('LinearMap', 3, 7)
    input('Better...')
    make_fig('BetterMap', 3, 7)
    input('Hash...')
    make_fig('HashMap', 3, 7)
