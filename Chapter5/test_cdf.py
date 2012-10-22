import time
import random
import matplotlib.pyplot as pyplot
import Cdf


def test_cdf(max_size):
    sizes = []
    times = []
    for n in range(1000, max_size, 10000):
        distr = [random.randint(1, 20) for each in range(n)]
        start = time.time()
        do_cdf = Cdf.MakeCdfFromList(distr)
        end = time.time()
        total_time = end - start
        sizes.append(n)
        times.append(total_time)
    print("Size  |  Time")
    for size, t in zip(sizes, times):
        print(size, "  |  ", t)
    return (sizes, times)


def graph_results(sizes, times):
    fitted_linear = fit(sizes, times, exp=1.0)
    pyplot.plot(sizes, times, 'bo', sizes, fitted_linear, 'r-')
    pyplot.xlabel('N')
    pyplot.ylabel('Time (s)')
    pyplot.show()


def fit(ns, ts, exp=1.0, index=-1):
    """Fits a curve with the given exponent.

    Use the given index as a reference point, and scale all other
    points accordingly.
    """
    nref = ns[index]
    tref = ts[index]

    tfit = []
    for n in ns:
        ratio = float(n) / nref
        t = ratio ** exp * tref
        tfit.append(t)
    return tfit


if __name__ == '__main__':
    res = test_cdf(10000)
    graph_results(*res)
