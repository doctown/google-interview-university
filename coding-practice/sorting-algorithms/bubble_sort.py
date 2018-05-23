def bubble_sort(array):
    count = 0
    for i in range(len(array)):
        for k in range(len(array)-1):
            if array[k] > array[k+1]:
                temp = array[k]
                array[k] = array[k+1]
                array[k+1] = temp
            count += 1
    return array


def TestSuite():
    numbers = [24, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(bubble_sort([24, 4, 1, 3, 9, 20, 25, 6, 21, 14], 3))
