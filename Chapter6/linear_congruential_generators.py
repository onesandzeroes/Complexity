import random
import subprocess


class LCG:
    """
    Abstract base class for all LCG's, to show which
    methods each implementation needs to implement.
    """

    def __init__(self, m, a, c, x0):
        """
        Initialize the generator with the values:

            m: the modulus
            a: the multiplier
            c: the increment
            x0: the seed/start value

        Which will be used to generate values according to
        the formula:
            x[n+1] = (a * x[n] + c) % m
        """
        self.index = 0
        self.m = m
        self.a = a
        self.c = c
        # Initialize the generator with x0
        self.current = x0

    def get_next(self):
        new_val = (self.a * self.current + self.c) % self.m
        return new_val

    def get_values(self, n):
        """
        Returns n values from the generator.
        """
        for i in range(n):
            self.current = self.get_next()
            yield self.current

    def get_bytes(self, n):
        for num in self.get_values(n):
            nb = num.to_bytes(4, 'little')
            yield nb


def test_LCG(m=2 ** 32, a=1664525, c=1013904223):
    seed = random.randrange(1, 6400)
    print("Starting LCG with seed: ", seed)
    lcg = LCG(m, a, c, seed)
    hundred_vals = list(lcg.get_values(100))
    print(hundred_vals)


def dieharder_test(m=2 ** 32, a=1664525, c=1013904223):
    seed = random.randrange(1, 6400)
    print("Starting LCG with seed: ", seed)
    lcg = LCG(m, a, c, seed)
    with open("generated_rands.txt", "w") as out:
        for each in lcg.get_values(2000):
            out.write(str(each) + "\n")


def dieharder_stdin(m=2 ** 32, a=1664525, c=1013904223):
    seed = random.randrange(1, 6400)
    diehard_args = ['dieharder', '-a', '-g', '200']
    lcg = LCG(m, a, c, seed)
    lots_of_vals = b''.join(list(lcg.get_bytes(10 ** 6)))
    with subprocess.Popen(
        diehard_args,
        stdin=subprocess.PIPE,
        shell=True
    ) as diehard:
        for nb in lots_of_vals:
            diehard.stdin.write(nb)


if __name__ == '__main__':
    dieharder_stdin()
    # dieharder_test()
    # test_LCG()
