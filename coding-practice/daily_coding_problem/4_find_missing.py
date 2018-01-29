"""
    Given an array of integers, find the first missing positive integer in
    linear time and constant space. In other words, find the lowest positive
    integer that does not exist in the array. The array can contain duplicates
    and negative numbers as well.

    For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0]
    should give 3.

    You can modify the input array in-place.
"""


# O(n) time; O(1) space
def find_missing(nums):
    hi = len(nums)
    lo = 1
    found_num = None

    for i in range(len(nums)):
        num = nums[i]
        while num >= lo and num <= hi and num != i + 1:
            swap(nums, i, num - 1)
            num = nums[i]

        if nums[i] != i + 1:
            nums[i] = 0

    for i in range(hi):
        if nums[i] == 0 and found_num is None:
            found_num = i + 1

    return found_num if found_num else hi + 1


def swap(array, x, y):
    temp = array[x]
    array[x] = array[y]
    array[y] = temp


def TestSuite():
    nums = [3, 4, -1, 1]
    out = 2
    actual = find_missing(nums)

    assert actual == out, "{} == {}".format(actual, out)

    nums = [1, 2, 0]
    out = 3
    actual = find_missing(nums)

    assert actual == out, "{} == {}".format(actual, out)

    print("Successfully completed test suite!")


if __name__ == "__main__":
    TestSuite()
