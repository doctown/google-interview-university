class BinarySort:
    def __init__(self, array):
        self.array = array

    def search(self, target):
        self.target = target
        return self.binary_search(self.array, 0, len(self.array) - 1)

    def binary_search(self, array, low, high):
        if (high < low):
            return None
        mid = (high + low) / 2

        if array[mid] == self.target:
            return mid
        elif self.target < array[mid]:
            return self.binary_search(array, low, mid - 1)
        else:
            return self.binary_search(array, mid + 1, high)

def TestSuite():
    numbers = [1, 2, 3, 4, 5, 6, 7]
    bs = BinarySort(numbers)

    assert(0  == bs.search(1))
    assert(3  == bs.search(4))
    assert(6  == bs.search(7))
    assert(None  == bs.search(8))

if __name__ == "__main__":
    TestSuite()
