from math import pi
from numpy import random
"""
    The area of a circle is defined as πr^2. Estimate π to 3 decimal places
    using a Monte Carlo method.

    Hint: The basic equation of a circle is x2 + y2 = r2.
"""
SAMPLE_SIZE = 30000


def pi_estimate():
    # randomly choose a range of numbers from 10 to 100000, by power of 10
    count_in = 0
    i = 0
    estimate = 0

    while abs(pi - estimate) > 0.001:
        i += 1
        power_of_10 = 10 ** i
        count_in = 0
        for k in range(power_of_10):
            # randomly choose an number between 1
            x = random.uniform()
            y = random.uniform()
            r = x**2 + y**2
            if r < 1:
                count_in += 1

        estimate = (count_in / power_of_10) * 4
    print(estimate)

if __name__ == "__main__":
    pi_estimate()
