"""
    Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

    For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

    • 10 = max(10, 5, 2)
    • 7 = max(5, 2, 7)
    • 8 = max(2, 7, 8)
    • 8 = max(7, 8, 7)

    Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.
"""
from queue import PriorityQueue


def find_max(arr, k):
    result = []
    heap = PriorityQueue()

    # insert k - 1 elements into heap
    for i in range(min(len(arr), k - 1)):
        heap.put((-arr[i], i))

    # add value and get max
    for i in range(k - 1, len(arr)):
        heap.put((-arr[i], i))
        found = False
        while not found:
            max_val, idx = heap.get()
            if (i - idx) < k:
                result.append(-max_val)
                heap.put((max_val, idx))
                found = True

    return result


def TestSuite():
    nums = [10, 5, 2, 7, 8, 7]
    k = 3
    expected = [10, 7, 8, 8]
    actual = find_max(nums, k)

    assert expected == actual, "{} == {}".format(expected, actual)

    print("Successfully completed")

if __name__ == "__main__":
    TestSuite()
