class MergeSort:
    def __init__(self):
        self.array = []

    def sort(self, array):
        #   split the array until you only have on, then sort
        self.array = array
        return self.merge_sort(self.array)

    def merge(self, left, right):
        sorted_array = []

        while len(left) > 0 or len(right) > 0:
            if len(left) > 0 and len(right) > 0:
                if (left[0] < right[0]):
                    sorted_array.append(left.pop(0))
                else:
                    sorted_array.append(right.pop(0))
            elif len(left) > 0:
                sorted_array.append(left.pop(0))
            else:
                sorted_array.append(right.pop(0))
        return sorted_array

    def merge_sort(self, array):
        if len(array) == 1:
            return array
        else:
            half = len(array) // 2
            return self.merge(self.merge_sort(array[0:half]), self.merge_sort(array[half:]))

if __name__ == "__main__":
    merge_sort = MergeSort()
    sorted = [1, 2, 3, 4, 5, 6]

    numbers = [1, 2, 3, 4, 5, 6]
    assert(merge_sort.sort(numbers) == sorted)

    numbers = [2, 5, 1, 3,  6, 4]
    assert(merge_sort.sort(numbers) == sorted)

    numbers = [6, 2, 5, 1, 3,  6, 4]
    sorted.append(6)
    assert(merge_sort.sort(numbers) == sorted)

