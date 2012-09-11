import os
import matplotlib.pyplot as pyplot


def etime():
    """
    See how much user and system time this process has used
    so far and return the sum
    """
    user, sys, chuser, chsys, real = os.times()
    return user + sys


def time_pluseq(n):
    """
    Takes an inputsize, n and concatenates n lists together,
    returning the time to perform the concatenation
    """
    lists = [[i] for i in range(n)]
    total = []
    start = etime()
    for each in lists:
        total += each
    end = etime()
    return end - start


def time_extend(n):
    """
    Takes an inputsize, n, and combines n lists using
    list.extend(), returning the time taken to perform the
    operation
    """
    lists = [[i] for i in range(n)]
    total = []
    start = etime()
    for each in lists:
        total.extend(each)
    end = etime()
    return end - start


def time_sum(n):
    lists = [[i] for i in range(n)]
    total = []
    start = etime()
    total = sum(lists, [])
    end = etime()
    return end - start


def graph_times(func):
    """
    Takes one of the timing functions defined in this file and graphs
    its input size/time relationship
    """
    x_vals = []
    for i in range(1, 10):
        x_vals.extend([i * 10 ** n for n in range(1, 7)])
    x_vals.sort()
    y_vals = [func(x) for x in x_vals]

    pyplot.plot(x_vals, y_vals)
    scale = 'log'
    pyplot.xscale(scale)
    pyplot.yscale(scale)
    pyplot.title('Sum of lists using +=')
    pyplot.xlabel('n')
    pyplot.ylabel('run time (s)')
    pyplot.show()

if __name__ == '__main__':
    print("Graphing plusequals:")
    graph_times(time_pluseq)
    input()
    print("Graphing extend:")
    graph_times(time_extend)
    input()
    print("Graphing sum:")
    graph_times(time_sum)
    input("Done! Press ENTER to exit")
