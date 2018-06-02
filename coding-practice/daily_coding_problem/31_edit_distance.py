"""
The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
"""


def edit_distance(first_word, second_word):
    T = [[0] * (len(second_word) + 1) for _ in range(len(first_word) + 1)]
    for i in range(len(T)):
        T[i][0] = i

    for i in range(len(T[0])):
        T[0][i] = i

    T[0][0] = 0

    for first_word_index in range(1, len(T)):
        for second_word_index in range(1, len(T[0])):
            # if letters the same then pre of both
            T[first_word_index][second_word_index] = T[first_word_index - 1][second_word_index - 1] if first_word[first_word_index - 1] == second_word[second_word_index - 1] else min(T[first_word_index][second_word_index - 1], T[first_word_index - 1][second_word_index], T[first_word_index - 1][second_word_index - 1]) + 1

    return T[-1][-1]


def TestSuite():
    first_string = "kitten"
    second_string = "kitten"
    expected = 0
    actual = edit_distance(first_string, second_string)

    assert expected == actual, "{} == {}".format(expected, actual)

    first_string = "kitten"
    second_string = "kite"
    expected = 2
    actual = edit_distance(first_string, second_string)

    assert expected == actual, "{} == {}".format(expected, actual)

    first_string = "sit"
    second_string = "sitting"
    expected = 4
    actual = edit_distance(first_string, second_string)

    assert expected == actual, "{} == {}".format(expected, actual)

    first_string = "kitten"
    second_string = "sitting"
    expected = 3
    actual = edit_distance(first_string, second_string)

    assert expected == actual, "{} == {}".format(expected, actual)

    print("Done")


TestSuite()



