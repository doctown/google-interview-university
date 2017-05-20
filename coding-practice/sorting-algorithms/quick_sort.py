class QuickSort:
    def sort(self, array):
        # call quick sort with the last number as the pivot
        self.quick_sort(array, 0, len(array) - 1)

    def quick_sort(self, array, low, high):
        if (low >= high):
            return
        # select the pivot
        pivot = high
        # set the new pivot index to lo
        new_pivot_index = low

        # compare pivot from lo to high
        for i in range(low, high  + 1):
            # swap, and update new pivot index
            if array[i] < array[pivot]:
                array[i], array[new_pivot_index] = array[new_pivot_index], array[i]
                new_pivot_index += 1
        array[pivot], array[new_pivot_index] = array[new_pivot_index], array[pivot]
        half = (low + high) // 2
        self.quick_sort(array, 0, half)
        self.quick_sort(array, half + 1, high)

def TestSuite():
    qs = QuickSort()
    sorted_list = [1, 2, 3, 4, 5, 6, 7]

    unsorted = [7, 6, 5, 4, 3, 2, 1]
    qs.sort(unsorted)
    assert(sorted_list == unsorted)

    unsorted = [3, 1, 4, 2, 7, 6, 5]
    qs.sort(unsorted)
    assert(sorted_list == unsorted)

    unsorted = [1, 2, 3, 4, 5, 6, 7]
    qs.sort(unsorted)
    assert(sorted_list == unsorted)

if __name__ == "__main__":
    TestSuite()
