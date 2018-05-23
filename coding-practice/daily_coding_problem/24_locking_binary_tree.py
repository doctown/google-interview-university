"""
Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

• is_locked, which returns whether the node is locked
• lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
• unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.

You may augment the node to add parent pointers or any other property you would like. You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes. Each method should run in O(h), where h is the height of the tree.

               F 8F F
               /  \
          F 4 T    F 10T F
           / \       /
        F 2F T T 6 T T 9 T
        /
      T 0 F
      /     \
    T -1 T  F 1 F
"""


LEFT = 'l'
RIGHT = 'r'

from collections import deque

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.locked = False
        self.can_lock_right = True
        self.can_lock_left = True
        self.parent = None

    def __str__(self):
        return str(self.value)

class BinaryTree(object):
    def __init__(self, value=None):
        self.root = Node(value) if value else value

    def is_locked(self, node):
        # is_locked, which returns whether the node is locked
        return node.locked

    def lock(self, node):
        # lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
        stack = deque()

        can_lock = not node.locked

        if node.parent:
            stack.append((node.parent, node))

        # check parents all can_lock is True
        while stack:
            parent, child = stack.pop()

            if parent.left == child:
                can_lock |= parent.can_lock_left
                can_lock &= parent.locked
            else:
                can_lock |= parent.can_lock_right
                can_lock &= parent.locked

            if child.parent:
                stack.append(child.parent)

        # if true, lock, then can_lock of parents is False
        # if a child is locked, all parent will say cannot lock for that side
        # if a parent is locked, it will show locked
        if can_lock:
            node.locked = True
            node.can_lock_left = False
            node.can_lock_right = False

            if node.parent:
                stack.append((node.parent, node))

            while stack:
                parent, child = stack.pop()
                if parent.left == child:
                    parent.can_lock_left = False
                else:
                    parent.can_lock_right = False

                if child.parent:
                    stack.append(child.parent)

        return can_lock

    def unlock(self, node):
        # unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.
        if node.locked:
            node.locked = True

            self.visitParents(node, lambda dir, p: p.can_lock_left = False if dir == LEFT else parent.can_lock_right = False)

            return True
        else:
            return False

    def visitParents(self, node, action):
        stack = deque()
        if node.parent:
            stack.append((node.parent, node))

        while stack:
            parent, child = stack.pop()
            if parent.left == child:
                action(LEFT, parent)
            else:
                action(RIGHT, parent)

            if child.parent:
                stack.append(child.parent)


def TestSuite():
    tree = BinaryTree(8)

    tree.left = Node(4)
    tree.left.parent = tree.root
    tree.left.right = Node(6)
    tree.left.left = Node(2)
    tree.left.right.parent = tree.left
    tree.left.left.parent = tree.left

    tree.right = Node(10)
    tree.right.left = Node(9)
    tree.right.parent = tree.root
    tree.right.left.parent = tree.right

    assert tree.is_locked(tree.left) is False

    assert tree.lock(tree.left), "{}".format(tree.left.value)
    assert tree.is_locked(tree.left), "{}".format(tree.left.value)

    assert tree.lock(tree.left.left) is False, "{}".format(tree.left.left)

    assert tree.lock(tree.root) is False, "{}".format(tree.root)

    assert tree.unlock(tree.left.left) is False, "{}".format(tree.left.left)

    print("Done")

if __name__ == "__main__":
    TestSuite()
