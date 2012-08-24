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
    lists = [['a'] for i in range(n)]
    total = []
    start = etime()
    for each in lists:
        total += each
    end = etime()
    return end - start

x_vals = []
for i in range(1, 10):
    x_vals.extend( [i * 10 ** n for n in range(1, 6)] )
y_vals = [time_pluseq(x) for x in x_vals]

pyplot.plot(x_vals, y_vals)
scale = 'log'
pyplot.xscale(scale)
pyplot.yscale(scale)
pyplot.title('Sum of lists using +=')
pyplot.xlabel('n')
pyplot.ylabel('run time (s)')
pyplot.show()
input()

