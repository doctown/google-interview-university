"""
  Given an array of integers, return a new array such that each element at
  index i of the new array is the product of all the numbers in the original
  array except the one at i. Solve it without using division and in O(n) time.

  For example, if our input was [1, 2, 3, 4, 5], the expected output would
  be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output
  would be [2, 3, 6].
"""


def num_product(nums):

    left = [1]
    right = [0] * (len(nums) - 1) + [1]

    for i in range(1, len(nums)):
        left.append(nums[i - 1] * left[i-1])

    for i in range(len(nums) - 2, -1, -1):
        right[i] = right[i + 1] * nums[i + 1]

    return [l * r for l, r in zip(left, right)]


def assertEquals(actual, output):
    assert actual == output, "{} == {}".format(actual, output)


def TestSuite():
    nums = [1, 2, 3, 4, 5]
    output = [120, 60, 40, 30, 24]
    actual = num_product(nums)

    assertEquals(actual, output)

    nums = [3, 2, 1]
    output = [2, 3, 6]
    actual = num_product(nums)

    assertEquals(actual, output)


if __name__ == "__main__":
    TestSuite()
