;""
    An implementation of dynamic array.
"""
MULTIPLIER = 2
DEFAULT_CAPACITY = 16


class Array:
    def __init__(self):
        self.array = [None for i in range(DEFAULT_CAPACITY)]
        self._size = 0
        self._capacity = DEFAULT_CAPACITY

    def size(self):
        return self._size

    def capacity(self):
        return self._capacity

    def is_empty(self):
        return self._size == 0

    def at(self, index):
        self.validateIndex(index)

        return self.array[index]

    def push(self, item):
        self._resize(None)

        self.array[self._size] = item
        self._size += 1

    def insert(self, index, item):
        self.validateIndex(index)
        self._resize(None)

        for i in range(self._size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = item

    def validateIndex(self, index):
        if index >= self._size:
            raise ValueError("Index is out of bounds")

    def prepend(self, item):
        # can use insert above at index 0
        pass

    def pop(self):
        if self._size == 0:
            raise ValueError("Cannot pop an empty array")
        if self._size < self._capacity / 4:
            self._resize(self._capacity / MULTIPLIER)

        self._size -= 1
        return self.array[self._size]

    def delete(self, index):
        # delete item at index, shifting all trailing elements left
        self.validateIndex(index)

        item = self.array[index]
        for i in range(index, self._size):
            self.array[i] = self.array[i + 1]

        self._size -= 1
        return item

    def remove(self, item):
        #  - looks for value and removes index holding it (even if in
        # multiple places)
        pass

    def find(self, item):
        # looks for value and returns first index with that value,
        # -1 if not found
        pass

    def _resize(self, new_capacity):
        """
            - private function
            - when you reach capacity, resize to double the size
            - when popping an item, if size is 1/4 of capacity, resize to half
        """
        pass


class TestSuite:
    def testAdd(self):
        array = Array()
        # empty
        assert array.is_empty()
        assert array.size() == 0, "{}".format(array.size())
        # add several
        array.push(1)
        assert not array.is_empty()
        assert array.size() == 1, "{}".format(array.size())
        array.push(2)
        assert array.size() == 2
        array.insert(0, 0)
        for i in range(3):
            assert array.at(i) == i, "expected {} but got {}".format(array.at(i), i)
            assert array.find(i) == i, "expected {} but got {}".format(array.find(i), i)
        assert array.find(4) == -1, "expected {} but got {}".format(array.find(4), -1)

    def testRemove(self):
        array = Array()
        # remove 1 in empty list
        try:
            assert 1 == array.pop()
        except ValueError as e
            assert True, e
        for i in range(3):
        array.push(1)
        assert array.size() == 2, "{}".format(array.size())

    def testResize(self):
        array = Array()
        assert array._capacity == DEFAULT_CAPACITY

    def run(self):
        self.testAdd()
        self.testRemove()
        self.testResize()


if __name__ == "__main__":
    suite = TestSuite()
    suite.run()
