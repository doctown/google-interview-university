"""
Write a function to return if two words are exactly "one edit" away, where an edit is:
Inserting one character anywhere in the word (including at the beginning and end)
Removing one character
Replacing exactly one character
"""


def one_edit(stringA, stringB):
    edits = [[0] * (len(stringB) + 1) for _ in range(len(stringA) + 1)]

    for i in range(len(stringB) + 1):
        edits[0][i] = i

    for i in range(len(stringA) + 1):
        edits[i][0] = i

    for a in range(1, len(stringA) + 1):
        for b in range(1, len(stringB) + 1):
            if stringA[a - 1] == stringB[b - 1]:
                edits[a][b] = edits[a - 1][b - 1]
            else:
                edits[a][b] = 1 + min(edits[a - 1][b], edits[a][b - 1])

    return edits[len(stringA)][len(stringB)] < 2


def TestSuite():
    stringA = 'oe'
    stringB = 'ode'
    output = True
    actual = one_edit(stringA, stringB)

    assert output == actual, "{} == {}".format(output, actual)

    stringA = 'ones'
    stringB = 'ode'
    output = False
    actual = one_edit(stringA, stringB)

    assert output == actual, "{} == {}".format(output, actual)

    print("Done")


if __name__ == "__main__":
    TestSuite()
