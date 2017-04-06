import math
class Heap():
  def __init__(self, array):
    self.array = array
    self.heap = self.heapInsert(self.array)

  def sort(self):
    sorted_array = []

    while len(self.heap) > 0:
      sorted_array.append(self.getMin())

    return sorted_array

  def heapInsert(self, array):
    heap = []
    for num in array:
      heap.append(num)
      self.bubbleUp(heap, len(heap) - 1)

    return heap

  def getParent(self, i):
    return math.ceil(i / 2) - 1

  def getChild(self, i):
    return i * 2 + 1

  def bubbleUp(self, heap, idx):
    parent_idx = self.getParent(idx)

    if parent_idx != -1 and heap[parent_idx] > heap[idx]:
      self.swap(heap, idx, parent_idx)
      self.bubbleUp(heap, parent_idx)

  def bubbleDown(self, heap, idx):
    child_idx = self.getChild(idx)
    other_child_idx = child_idx + 1

    if child_idx < len(heap) and  heap[idx] > heap[child_idx]:
        self.swap(heap, idx, child_idx)
        self.bubbleDown(heap, child_idx)
    elif other_child_idx < len(heap) and heap[idx] > heap[other_child_idx]:
        self.swap(heap, idx, other_child_idx)
        self.bubbleDown(heap, other_child_idx)

  def swap(self, heap, i , k):
    heap[k], heap[i] = heap[i], heap[k]

  def getMin(self):
    min_num = None

    if len(self.heap) > 0:
      min_num = self.heap.pop(0)
      if len(self.heap) > 0:
        self.bubbleDown(self.heap, 0)

    return min_num

def testSuite():
  sorted_numbers = [1, 2, 3, 4, 5]
  unsorted_numbers = [3, 5, 2, 1, 4]
  duplicate_numbers = [7, 3, 5, 4, 2, 1, 4]

  heap = Heap(sorted_numbers)
  actual = heap.sort()
  assert(actual == sorted_numbers)

  heap = Heap(unsorted_numbers)
  actual = heap.sort()
  assert(actual == sorted_numbers)

  heap = Heap(duplicate_numbers)
  actual = heap.sort()
  assert(actual == [1, 2, 3, 4, 4, 5, 7])

if __name__ == "__main__":
  testSuite()

