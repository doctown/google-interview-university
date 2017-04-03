import sys
MAX_VALUE = sys.maxsize

def sort(array):
    for index_array in range(len(array)):
        index_min, min = findMinimum(index_array, array)
        swap(index_array, index_min, array)
    return array

def swap(i, k, array):
    array[i], array[k] = array[k], array[i]

def findMinimum(index, array):
    smallest = MAX_VALUE
    min_index = 0

    for i in range(index, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            min_index = i

    return [min_index, smallest]

def testSuite():
    sorted_numbers = [1, 2, 3, 4, 5]
    unsorted_numbers = [3, 5, 2, 1, 4]
    duplicate_numbers = [7, 3, 5, 4, 2, 1, 4]

    actual = sort(sorted_numbers)
    assert(actual == sorted_numbers)

    actual = sort(unsorted_numbers)
    assert(actual == sorted_numbers)

    actual = sort(duplicate_numbers)
    assert(actual == [1, 2, 3, 4, 4, 5, 7])

if __name__ == "__main__":
    testSuite()


