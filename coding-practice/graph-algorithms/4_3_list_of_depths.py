class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def addNodeToList(node, linkedList, level):
    node = Node(node.value)
    if linkedList.get(level) is not None:
        node.next = linkedList[level]
    linkedList[level] = node


def convertBinaryTree(tree):
    if tree is None:
        return

    linkedList = {}
    q = [{'node': 'tree', 'depth': 0}]

    while len(q) != 0:
        node, level = q.pop()
        addNodeToList(node, linkedList, level)

        if node.left:
            q.append({'node': node.left, 'depth': level})
        if node.right:
            q.append({'node': node.right, 'depth': level})

    return linkedList

def TestSuite():
    # TODO: Add test
