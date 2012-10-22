# Using the complimentary distribution of a sample to check if it's
# exponentially distributed
import random
import math
import matplotlib.pyplot as pyplot
import Cdf


def plot_ccdf(values, probs, title='', lambd=0):
    """
    Plot the complimentary CDF (1 - CDF) of a given set of values and
    probabilities, to check if it's exponentially distributed, i.e.
    log(y) = -lambda * x (where lambda determines the mean and variance
    of the distribution)
    """
    ccdf_x = [(1 - p) for p in probs]
    log_ys = [math.log(y) if y > 0 else None for y in ccdf_x]
    lambda_fit = [(x * -lambd) for x in values]
    pyplot.plot(values, log_ys, 'ro', values, lambda_fit, 'b-')
    pyplot.ylabel("Log(y)")
    pyplot.title(title)
    pyplot.show()


def test_ccdf(size):
    expo_sample = [random.expovariate(0.2) for n in range(size)]
    expo_cdf = Cdf.MakeCdfFromList(expo_sample)
    plot_ccdf(*expo_cdf.Render(), title="Exponential Sample", lambd=0.2)
    normal_sample = [random.gauss(5, 1) for n in range(size)]
    normal_cdf = Cdf.MakeCdfFromList(normal_sample)
    plot_ccdf(*normal_cdf.Render(), title="Normal Sample", lambd=0.2)

if __name__ == '__main__':
    test_ccdf(10000)
