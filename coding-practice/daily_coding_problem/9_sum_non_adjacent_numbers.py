"""
    Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.

For example, [2, 4, 6, 8] should return 12, since we pick 4 and 8. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
"""


def sum_numbers(nums):
    if len(nums) == 0:
        return
    sums = [0, nums[0]]

    for i in range(2, len(nums) + 1):
        sums.append(max(sums[i - 2] + nums[i-1], sums[i-1]))

    return max(sums[-2:])


def TestSuite():
    nums = [2, 4, 6, 8]
    output = 12
    actual = sum_numbers(nums)

    assert output == actual,"{} == {}".format(output, actual)

    nums = [5, 1, 1, 5]
    output = 10
    actual = sum_numbers(nums)

    nums = []
    output = None
    actual = sum_numbers(nums)

    nums = [10]
    output = 10
    actual = sum_numbers(nums)

    print("Successful")
    assert output == actual,"{} == {}".format(output, actual)

if __name__ == "__main__":
    TestSuite()
