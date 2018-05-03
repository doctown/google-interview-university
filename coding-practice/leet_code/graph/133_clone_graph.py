"""
    Clone an undirected graph. Each node in the graph contains a label and
    a list of its neighbors.
"""


# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None or node == {}:
            return node

        clone = UndirectedGraphNode(node.label)
        for connected_node in node.neighbors:
            # handle a node is a neighbor of itself
            if node.label == connected_node.label:
                clone.neighbors.append(UndirectedGraphNode(connected_node.label))
            if not self.contains(clone.neighbors, connected_node):
                clone.neighbors.append(self.cloneGraph(connected_node))
            else:
                clone.neighbors.append(UndirectedGraphNode(connected_node.label))

        return clone

    def contains(self, neighbors, node):
        found = False
        for connected_node in neighbors:
            if connected_node.label == node.label:
                found = True
        return found

    def find(self, neighbors, node):
        for connected_node in neighbors:
            if (node.label == connected_node.label):
                return connected_node

    def testSuite(self):
        # {0,1,2#1,2#2,2}
        zero = UndirectedGraphNode(0)
        zero.neighbors.append(zero)
        zero.neighbors.append(zero)
        # one = UndirectedGraphNode(1)
        # two = UndirectedGraphNode(2)
        # zero.neighbors.append(one)
        # zero.neighbors.append(two)
        # zero.neighbors.append(two)
        # one.neighbors.append(two)
        # two.neighbors.append(two)

        clone = self.cloneGraph(zero)
        print(clone.neighbors)
        assert len(clone.neighbors) == 3
        assert len(clone.neighbors[0].neighbors) == 1
        assert len(clone.neighbors[1].neighbors) == 1, clone.neighbors[1].neighbors
        print("Pass")


if __name__ == "__main__":
    sol = Solution()
    sol.testSuite()
