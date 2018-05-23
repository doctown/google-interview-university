"""
Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
"""


class LinkedList(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def remove_kth(head, k):
    end = head

    for _ in range(k + 1):
        end = end.next

    kth = head

    while end:
        end = end.next
        kth = kth.next

    kth.next = kth.next.next

    return head


def TestSuite():
    head = LinkedList(1)
    head.next = LinkedList(2)
    head.next.next = LinkedList(3)
    head.next.next.next =  LinkedList(4)
    head.next.next.next.next =  LinkedList(5)

    new_head = remove_kth(head, 2)

    assert head.value == 1
    assert head.next.value == 2
    assert head.next.next.value == 3
    assert head.next.next.next.value == 5

    head = LinkedList(1)
    head.next = LinkedList(2)
    head.next.next = LinkedList(3)
    head.next.next.next =  LinkedList(4)
    head.next.next.next.next =  LinkedList(5)

    new_head = remove_kth(head, 1)

    assert head.value == 1
    assert head.next.value == 2
    assert head.next.next.value == 3
    assert head.next.next.next.value == 4

    print("Done")

TestSuite()
