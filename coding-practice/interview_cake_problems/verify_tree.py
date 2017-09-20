"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
write a function to check whether these edges make up a valid tree.
For example:
    Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.
    [0: 1, 2, 3]
    [1: 4]
    Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.
    [0: 1]
    [1: 2, 3, 4]
    [2: 3]
    Given n = 6 and edges = [[0, 1], [1, 2], [3, 4], [4. 5] return false.
    [0: 1]
    [1: 2]
    [3: 4]
    [4, 5]
    {
        1: 0,
        2: 1,
        3: 4,
        5: 4
    }
    Every child can only have one parent
    Every node is connect to one root ???
"""
# O(n)
def checkTree(edges):
    parent = {}
    list = {}

    for edge in edges:
        p = edge[0]
        c = edge[1]
        if parent.get(c):
            return False
        else:
            parent[c] = p
        if list.get(p):
            list[p].append(c)
        else:
            list[p] = [c]

    count = 0
    for k, v in list.items():
        if parent.get(k) == None:
            count += 1

    return True if count <= 1 else False

def testSuite():
    n = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    expected = True
    actual = checkTree(edges)

    assert expected == actual, "expected is {0}, but actual is {1}".format(expected, actual)

    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    expected = False
    actual = checkTree(edges)

    assert expected == actual, "expected is {0}, but actual is {1}".format(expected, actual)

    n = 6
    edges = [[0, 1], [1, 2], [3, 4], [4, 5]]
    expected = False
    actual = checkTree(edges)
    assert expected == actual, "expected is {0}, but actual is {1}".format(expected, actual)
if __name__ == "__main__":
    testSuite()
