"""
[1, 2, 3, 4, 5]
"""
def newStack(stack):
  q = []
  num_of_elements = len(stack)
  count = 1

  while (count < num_of_elements):
    for i in range(count, len(stack)):
      q.append(stack.pop())
    for i in range(len(q)):
      stack.append(q.pop(0))
    count += 1

  return stack

def newStack2(stack):
  """
    Initial attempt accessing beginning and end of stack
  """
  q = []

  while (len(stack) > 0):
    q.append(stack.pop(0))
    if len(stack) > 0:
      q.append(stack.pop())
  return q

def testSuite():
  stack = [1, 2, 3, 4, 5]
  actual = newStack(stack)
  expected =  [1, 5, 2, 4, 3]

  assert actual == expected, "{} == {}".format(actual, expected)

  stack = [1, 2, 3, 4]
  actual = newStack(stack)
  expected = [1, 4, 2, 3]

  assert actual == expected, "{} == {}".format(actual, expected)

  print("Test successfully completed")

if __name__ == "__main__":
  testSuite()
