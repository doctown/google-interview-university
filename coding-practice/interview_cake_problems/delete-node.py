class LinkedListNode:
  def __init__(self, value):
    self.value = value
    self.next  = None

def delete_node(node):
  if (node == None or node.next is None):
    node.value = None
    node.next = None
  else:
    node.value = node.next.value
    node.next = node.next.next

a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c

delete_node(b)

assert(a.next.value == c.value)
assert(a.next.next == c.next)
