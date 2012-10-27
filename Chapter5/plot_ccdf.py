# Using the complimentary distribution of a sample to check if it's
# exponentially distributed
import random
import math
import matplotlib.pyplot as pyplot
import Cdf


def plot_ccdf_exp(values, probs, title='', lambd=0):
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


def test_ccdf_exp(size):
    expo_sample = [random.expovariate(0.2) for n in range(size)]
    expo_cdf = Cdf.MakeCdfFromList(expo_sample)
    plot_ccdf_exp(*expo_cdf.Render(), title="Exponential Sample", lambd=0.2)
    normal_sample = [random.gauss(5, 1) for n in range(size)]
    normal_cdf = Cdf.MakeCdfFromList(normal_sample)
    plot_ccdf_exp(*normal_cdf.Render(), title="Normal Sample", lambd=0.2)


def plot_ccdf_pareto(values, probs, alpha=0):
    """
    Plot log(x) against log(ccdf(x)) for a quick check of whether a sample
    is Pareto-distributed- should give a straight line with a slope of
    -alpha (where alpha determines the shape of the distribution) and
    an intercept of alpha * log(x_m) (where x_m determines the location
    of the distribution)
    """
    log_xs = [math.log(x) for x in values]
    ys = [(1 - p) for p in probs]
    log_ys = [math.log(y) if y > 0 else None for y in ys]
    fitted_line = [(-1 * alpha * x) for x in log_xs]
    pyplot.plot(values, ys, 'ro')
    pyplot.title("Raw CCDF")
    pyplot.xlabel("x")
    pyplot.ylabel("CCDF(x)")
    pyplot.show()
    pyplot.plot(log_xs, log_ys, 'ro', log_xs, fitted_line, 'b-')
    pyplot.xlabel("Log(x)")
    pyplot.ylabel("Log(y)")
    pyplot.show()


def test_ccdf_pareto(size, alpha):
    pareto_sample = [random.paretovariate(alpha) for n in range(size)]
    pareto_cdf = Cdf.MakeCdfFromList(pareto_sample)
    plot_ccdf_pareto(*pareto_cdf.Render(), alpha=alpha)

if __name__ == '__main__':
    test_ccdf_pareto(10000, 2)
