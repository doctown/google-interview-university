class Node:
    def __init__(self, name, neighbors):
        self.name = name
        self.neighbors = []


def find_path(start, end, visited):
    if start.name == end.name:
        return True
    if start in visited:
        return False
    visited.add(start)
    return any(find_path(child, end, visited) for child in start.neighbors)


def path_exists(node_a, node_b):
    found = find_path(node_a, node_b, set())
    if not found:
        found = find_path(node_b, node_a, set())

    return found


def testSuite():
    a = Node('a', [])
    b = Node('b', [])
    c = Node('c', [])
    d = Node('d', [])
    f = Node('f', [])
    i = Node('i', [])

    a.neighbors.append(b)
    b.neighbors.append(d)
    b.neighbors.append(f)
    c.neighbors.append(a)
    i.neighbors.append(f)

    assert path_exists(a, d)
    assert path_exists(b, a)
    assert not path_exists(c, i)

    print("Pass")


testSuite()
