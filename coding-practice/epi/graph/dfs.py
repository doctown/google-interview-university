"""
DFS with adjacency list (recursive)
DFS with adjacency list (iterative with stack)
DFS with adjacency matrix (recursive)
DFS with adjacency matrix (iterative with stack)
"""


class Graph:
    """
        {
            'a': ['b', 'c']
            'b': []
            'c': 'a'
        }
    """
    def __init__(self, numOfVertices=3):
        self.list = {}
        self.n = numOfVertices
        self.matrix = [[0] * self.n for _ in range(self.n)]

    def addEdge(self, fro, to):
        if self.list.get(fro) is None:
            self.list[fro] = []
        if self.list.get(to) is None:
            self.list[to] = []
        if to not in self.list[fro]:
            self.list[fro].append(to)

        self.matrix[fro][to] = 1


def alRecurDFS(graph):
    visited = set()
    for vertex in graph.list:
        dfsRecur(graph, vertex, lambda ch: print(ch), visited)


def dfsIter(graph):
    visited = set()
    for firstNode in graph.list:
        if firstNode in visited:
            continue
        stack = []
        stack.append(firstNode)

        while len(stack) != 0:
            node = stack.pop()
            visited.add(node)
            print(node)

            for child in graph.list[node]:
                if child not in visited and child not in stack:
                    stack.append(child)


def dfsIterMatrix(graph):
    stack = []
    visited = set()
    for row in range(len(graph.matrix)):
        if row not in visited:
            stack.append(row)

        while len(stack) != 0:
            node = stack.pop()
            print(node)
            visited.add(node)

            for childIndex in range(len(graph.matrix[node])):
                if graph.matrix[node][childIndex] == 1 and childIndex not in visited:
                    stack.append(childIndex)


def dfsRecur(g, node, func, visitied):
    if node in visitied:
        return
    visitied.add(node)
    func(node)

    for child in g.list[node]:
        dfsRecur(g, child, func, visitied)


def mRecur(graph):
    visited = set()

    for idx in range(len(graph.matrix)):
        dfsRecurMatrix(graph, idx, lambda ch: print(ch), visited)


def dfsRecurMatrix(g, nodeIndex, func, visited):
    if nodeIndex in visited:
        return
    visited.add(nodeIndex)
    func(nodeIndex)

    for childIndex in range(len(g.matrix[nodeIndex])):
        if g.matrix[nodeIndex][childIndex] == 1:
            dfsRecurMatrix(g, childIndex, func, visited)


def TestSuite():
    g = Graph(5)
    g.addEdge(1, 4)
    g.addEdge(4, 3)
    g.addEdge(1, 2)
    g.addEdge(2, 4)
    g.addEdge(2, 1)

#    alRecurDFS(g)
    # mRecur(g)
    # dfsIter(g)
    dfsIterMatrix(g)


if __name__ == "__main__":
    TestSuite()
