"""
[1] Given an array of integers, determine whether or not there exist two elements in the array (at different positions) whose sum is equal to some target value. Examples: [5, 4, 2, 4], 8 --> true [5, 1, 2, 4], 8 --> false
use a set

"""
from bisect import bisect_left


# copied from stackflow
def binary_search(a, x, lo=0, hi=None):  # can't use a to specify default for hi
    hi = hi if hi is not None else len(a)  # hi defaults to len(a)
    pos = bisect_left(a, x, lo, hi)  # find insertion position
    return (pos if pos != hi and a[pos] == x else -1)


def two_element_sum(numbers, target):
    sorted_numbers = sorted(numbers)

    for i in range(len(sorted_numbers)):
        num = sorted_numbers[i]
        diff = abs(target - num)
        if binary_search(sorted_numbers[:i] + sorted_numbers[i + 1:], diff) != -1:
            return True

    return False


def TestSuite():
    numbers = [5, 4, 2, 4]
    target = 8
    output = True
    actual = two_element_sum(numbers, target)

    assert output == actual, "{} == {}".format(output, actual)

    numbers = [5, 1, 2, 4]
    target = 8
    output = False
    actual = two_element_sum(numbers, target)

    assert output == actual, "{} == {}".format(output, actual)

    print("Successful")

TestSuite()
