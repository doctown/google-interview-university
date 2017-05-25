"""
    Based on code from Algorithm Design Manual
    Original Author: Skeena
"""

def quicksort(array, lo, hi):
    if hi - lo > 0:
        p = partition(array, lo, hi)
        quicksort(array, lo, p - 1)
        quicksort(array, p + 1, hi)

def partition(array, lo, hi):
    pivot = hi
    firstHigh = lo

    for i in range(lo, hi):
        if array[i] < array[pivot]:
            array[i], array[firstHigh] = array[firstHigh], array[i]
            firstHigh += 1
    array[pivot], array[firstHigh] = array[firstHigh], array[pivot]

    return firstHigh

sorted_list = [1, 2, 3, 4, 5, 6, 7]

unsorted = [7, 6, 5, 4, 3, 2, 1]
quicksort(unsorted, 0, len(unsorted) - 1)
assert(sorted_list == unsorted)

unsorted = [3, 1, 4, 2, 7, 6, 5]
quicksort(unsorted, 0, len(unsorted) - 1)
assert(sorted_list == unsorted)

unsorted = [1, 2, 3, 4, 5, 6, 7]
quicksort(unsorted, 0, len(unsorted) - 1)
assert(sorted_list == unsorted)

