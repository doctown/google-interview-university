"""
A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.
"""


# O(n^3) time, O(n**2) space
def best_cost(matrix):
    best = [[0] * (len(matrix[0])) for _ in range(len(matrix) + 1)]
    for i in range(len(matrix[0])):
        best[1][i] = matrix[0][i]

    for i in range(2, len(matrix) + 1):
        for k in range(len(matrix[0])):
            best[i][k] = matrix[i-1][k] + min(best[i-1][:k] + best[i-1][k+1:])

    print(best)
    return min(best[len(matrix)])


def TestSuite():
    matrix = [[1, 0],
              [1, 0],
              [1, 5]]
    expected = 2
    actual = best_cost(matrix)

    assert expected == actual, "{} == {}".format(expected, actual)

    print("Successfully completed")


if __name__ == "__main__":
    TestSuite()
