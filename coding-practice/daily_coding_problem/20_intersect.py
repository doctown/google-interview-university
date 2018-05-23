"""
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

"""


class Node(object):
    def __init__(self, value, child=None):
        self.value = value
        self.next = child


class LinkedList(object):
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head

    def addNode(self, node):
        self.tail.next = node
        self.tail = self.tail.next

    def add(self, value):
        self.tail.next = Node(value)
        self.tail = self.tail.next


def reverse_list(cur):
    prev = None

    while cur:
        last = cur
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node

    return last


def find_intersect(listA, listB):
    new_list = reverse_list(listA.head)

    cur = listB.head

    while cur:
        next_node = cur.next
        cur.next = None
        cur = next_node

    # make all None from listB
    cur = new_list

    while cur and cur.next:
        cur = cur.next

    return cur.value


def TestSuite():
    node = Node(8)
    node2 = Node(10)

    listA = LinkedList(3)
    listA.add(7)
    listA.addNode(node)
    listA.addNode(node2)

    listB = LinkedList(99)
    listB.add(1)
    listB.addNode(node)
    listB.addNode(node2)

    expected = 8
    actual = find_intersect(listA, listB)

    assert expected == actual, "{} == {}".format(expected, actual)



TestSuite()
