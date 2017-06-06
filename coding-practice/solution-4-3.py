# 4-3.  [3]
# Take a sequence of 2n real numbers as input. Design an O (n log n) algorithm that partitions the numbers into n pairs,
# with the property that the partition minimizes the maximum sum of a pair. For example, say we are given the numbers (1,3,5,9).
#
# The possible partitions are ((1,3),(5,9)), ((1,5),(3,9)), and ((1,9),(3,5)).
# The pair sums for these partitions are (4,14), (6,12), and (10,8).
# Thus the third partition has 10 as its maximum sum, which is the minimum over the three partitions.

def pairMinimizer(numbers):
    pairs = []

    # sort the numbers
    sorted_numbers = list(numbers)
    sorted_numbers.sort()

    # create pairs from the first and last number
    while len(sorted_numbers) > 0:
        pairs.append((sorted_numbers.pop(0), sorted_numbers.pop()))
    return pairs

def maxSum(numbers):
    max = sum(numbers[0])
    for pair in numbers:
        if (sum(pair) > max):
            max = sum(pair)
    return max

def TestSuite():
  num = (1, 3, 9, 5)
  result = pairMinimizer(num)
  assert(maxSum(result) == 10)


if __name__ == "__main__":
    TestSuite()
