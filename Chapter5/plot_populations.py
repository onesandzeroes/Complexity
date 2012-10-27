import math
import matplotlib.pyplot as pyplot
import Cdf
from populations import ReadData


def plot_pop_cdf():
    pops = ReadData()
    pops_cdf = Cdf.MakeCdfFromList(pops)
    raw_x, raw_cdf = pops_cdf.Render()
    pyplot.figure(1)
    pyplot.plot(raw_x, raw_cdf, 'ro')
    pyplot.title("Raw population CDF")
    pyplot.xlabel("Population")
    pyplot.figure(2)
    log_x = [math.log(x) for x in raw_x]
    pyplot.plot(log_x, raw_cdf, 'ro')
    pyplot.title("Log scale CDF")
    pyplot.xlabel("log(population)")
    pyplot.figure(3)
    ccdf = [(1 - cdf) for cdf in raw_cdf]
    log_ccdf = [math.log(y) if y > 0 else None for y in ccdf]
    pyplot.plot(log_x, log_ccdf, 'ro')
    pyplot.title("Log population vs Log ccdf")
    pyplot.show()


def plot_pop_cdf_upper():
    """
    According to Ioannides and Skouras (2012), populations are only
    Pareto-distributed above 60000 or so- check if that's true in this
    data
    """
    pops = ReadData()
    cut_pops = []
    for pop in pops:
        if pop > 600000:
            cut_pops.append(pop)
    pops_cdf = Cdf.MakeCdfFromList(cut_pops)
    raw_x, raw_cdf = pops_cdf.Render()
    log_x = [math.log(x) for x in raw_x]
    ccdf = [(1 - p) for p in raw_cdf]
    log_ccdf = [math.log(y) if y > 0 else None for y in ccdf]
    pyplot.plot(log_x, log_ccdf, 'ro')
    pyplot.show()




if __name__ == '__main__':
    plot_pop_cdf_upper()
    # plot_pop_cdf()
