class Tree(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def checkTree(tree, min_num, max_num):
    valid = True

    if tree:
        if tree.right:
            if tree.right.value > max_num:
                valid = checkTree(tree.right, None, tree.value)
            else:
                valid = False
        if valid and tree.left:
            if tree.left.value < min_num:
                valid &= checkTree(tree.left, tree.value, None)
            else:
                valid = False

    return valid


def validBST(tree):
    return checkTree(tree.left, tree.value, None) and checkTree(tree.right, None, tree.value)

def TestSuite():
    tree = Tree(4)
    tree.left = Tree(3)
    tree.right = Tree(2)

    output = False
    actual = validBST(tree)

    assert output == actual, "{} == {}".format(output, actual)

    tree = Tree(7)
    tree.left = Tree(4)
    tree.left.left = Tree(1)
    tree.left.right = Tree(5)
    tree.right = Tree(8)
    tree.right.right = Tree(20)
    tree.right.right.left = Tree(10)
    tree.right.right.right = Tree(30)

    output = True
    actual = validBST(tree)

    assert output == actual, "{} == {}".format(output, actual)

    tree = Tree(10)
    tree.left = Tree(5)
    tree.left.right = Tree(25)
    tree.left.right = Tree(20)

    output = False
    actual = validBST(tree)

    assert output == actual, "{} == {}".format(output, actual)

    print("Done")

TestSuite()
