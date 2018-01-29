"""
    An XOR linked list is a more memory efficient doubly linked list. Instead
    of each node holding next and prev fields, it holds a field named both,
    which is a XOR of the next node and the previous node. Implement a XOR
    linked list; it has an add(element) which adds the element to the end, and
    a get(index) which returns the node at index.

    If using a language that has no pointers (such as Python), assume you have
    access to get_pointer and dereference_pointer functions that converts
    between nodes and memory addresses.
"""
import ctypes
from operator import xor


class Node:
    def __init__(self, both, value):
        self.both = both
        self.value = value


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, element):
        node = Node(None, element)
        cur = self.head
        node_memory_pointer = dereference_pointer(node)

        if self.head is None:
            self.head = node
        elif self.head.both is None:
            self.head.both = node_memory_pointer
            node.both = dereference_pointer(self.head)
        else:
            cur = self.traverse_list()
            node.both = dereference_pointer(cur)
            cur.both = get_xor(node_memory_pointer, cur.both)

    def traverse_list(self):
            cur = self.head.next
            prev = dereference_pointer(self.head)

            while (cur.both is not None):
                next_memory_address = get_xor(prev, cur.both)
                prev = dereference_pointer(cur)
                cur = get_pointer(next_memory_address)

            return cur

    def get(self, index):
        cur_index = 0

        if self.head is None:
            return None
        elif index == 1:
            return self.head
        else:
            prev = 0
            cur = get_pointer(self.head.both) if self.head.both else None

            while (cur is not None and cur_index <= index):
                next_memory_pointer = get_xor(prev, cur.both)
                prev = dereference_pointer(cur)
                cur = get_pointer(next_memory_pointer)
                cur_index += 1

            return cur.value if cur else None


# converts a node into both value
def get_xor(prev, next_p):
    return xor(prev, next_p)


# returns the node at self memory address
def get_pointer(memory_address):
    ctypes.cast(id(memory_address), ctypes.py_object)


# return the memory address of self node
def dereference_pointer(node):
    id(node)
