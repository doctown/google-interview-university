def sort(array):
  for unsorted_index in range(1,len(array)):
    sorted_index = 0
    inserted = False
    while sorted_index < unsorted_index and not inserted:
      if array[unsorted_index] < array[sorted_index]:
        insert(sorted_index, unsorted_index, array)
        inserted = True
      sorted_index += 1
  return array

def insert(i, k, array):
  temp = array[k]
  for num in range(k, i, -1):
    array[num] = array[num - 1]
  array[i] = temp

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


