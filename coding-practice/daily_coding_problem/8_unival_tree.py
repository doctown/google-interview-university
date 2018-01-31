"""
    A unival tree (which stands for "universal value") is a tree where all nodes
    have the same value.

    Given the root to a binary tree, count the number of unival subtrees.
"""


class Node:
    def __init__(self, value):
        self.parent = None
        self.left = None
        self.right = None
        self.value = value


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)

        if not self.root:
            self.root = node
        else:
            cur = self.root

            while cur is not None:
                if cur.value == value:
                    if cur.left is None:
                        node.parent = cur
                        cur.left = node
                        cur = None
                    elif cur.right is None:
                        node.parent = cur
                        cur.right = node
                        cur = None
                    else:
                        cur = cur.left

                elif cur.value < value:
                    if cur.right:
                        cur = cur.right
                    else:
                        node.parent = cur
                        cur.right = node
                        cur = None
                else:
                    if cur.left:
                        cur = cur.left
                    else:
                        node.parent = cur
                        cur.left = node
                        cur = None

    def __str__(self):
        return self.preorder(self.root)

    def preorder(self, node):
        string = ""
        if node is not None:
            string += "(" + self.preorder(node.left)
            string += str(node.value)
            string += ")" + self.preorder(node.right)
        return string


def unival_tree_count(root):
    val = 0
    orig = 0
    if root is not None:
        key = root.value

        # check children for match,
        if root.left and root.left.value == key:
            orig = 1
            val += explore(root.left, key)
        elif root.left:
            val += unival_tree_count(root.left)

        if root.right and root.right.value == key:
            val += (orig & 1) + explore(root.right, key)
        elif root.right:
            val += unival_tree_count(root.right)
    return val


def explore(node, key):
    # if match, explore until no match, send unmatched child back to this function
    val = 0
    if node.left:
        if node.left.value == key:
            val += explore(node.left, key)
        else:
            val += unival_tree_count(node.left)
    elif node.right:
        if node.right.value == key:
            val += explore(node.right, key)
        else:
            val += unival_tree_count(node.right)

    return val


if __name__ == "__main__":
    tree = Tree()
    tree.insert(1)
    tree.insert(1)
    tree.insert(1)
    tree.insert(2)
    tree.insert(0)
    tree.insert(3)
    tree.insert(2)
    tree.insert(3)
    tree.insert(5)
    tree.insert(5)
    tree.insert(5)
    tree.insert(5)
    actual = unival_tree_count(tree.root)
    assert 2 == actual, "{} == {}".format(2, actual)
