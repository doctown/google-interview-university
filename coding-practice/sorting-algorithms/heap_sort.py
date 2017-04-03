def sort(array):
  heap = heapInsert(array)
  sorted_array = []

  while len(heap) > 0:
    sorted_array.append(getMin(heap))

  return sorted_array

def heapInsert(array):
  heap = []
  for i in array:
    heap.append(i)
    bubbleUp(heap)

  return heap

def getParent(heap, i):
  return i / 2 - 1

def getChild(heap, i):
  return i * 2 + 1

def bubbleUp(heap, idx):
  parent_idx = getParent(heap, idx)

  if heap[parent_idx] > heap[idx]:
    swap(heap, idx, parent_idx)
    idx = parent_idx
    parent_idx = getParent(heap, idx)
    bubbleUp(heap, idx)

def bubbleDown(heap, i):
  # TODO: Implement bubble down

def swap(heap, i , k):
  heap[k], heap[i] = heap[i], heap[k]

def getMin(heap):
  child = getChild(heap, 0)
  bubbleDown(heap, child)
  min_num = heap.pop()

  return min_num

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


