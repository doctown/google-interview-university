"""
    There exists a staircase with N steps, and you can climb up either 1 or 2
    steps at a time. Given N, write a function that returns the number of
    unique ways you can climb the staircase. The order of the steps matters.

    For example, if N is 4, then there are 5 unique ways:

    • 1, 1, 1, 1
    • 2, 1, 1
    • 1, 2, 1
    • 1, 1, 2
    • 2, 2

    What if, instead of being able to climb 1 or 2 steps at a time, you could
    climb any number from a set of positive integers X? For example, if
    X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""


def num_of_steps(N):
    n_1 = 0
    n_2 = 1

    for i in range(N):
        n_0 = n_1 + n_2
        n_1 = n_2
        n_2 = n_0

    return n_2 if N > 1 else n_1


def TestSuite():
    N = 4
    actual = num_of_steps(N)
    output = 5

    assert output == actual, "{} == {}".format(output, actual)

    print("Testing Successful")


if __name__ == "__main__":
    TestSuite()
