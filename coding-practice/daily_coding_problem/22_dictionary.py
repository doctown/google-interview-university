"""
Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

   a h e r
 a T F F F
 h - F T T
 e - - F F
 r - - - F

"""

def getWords(string, words, i):
    results = []

    while i > 2:
        for start in range(1, i-1):
            print(start, i)
            if words[start][i-1]:
                results.insert(0, string[start-1: i-1])
                i = start

    for w in words:
        print(w)
    return results


def get_sentence(dictionary, string):
    words = [[False] * (len(string) + 1) for _ in range(len(string) + 1)]
    results = None

    for i in range(len(words)):
        words[i][0] = True
        words[0][i] = True

    for i in range(1, len(string) + 1):
        for k in range(i, len(string) + 1):
            word = string[i-1:k]
            if word in dictionary:
                words[i][k] = word in dictionary
            else:
                words[i][k] = word in dictionary and any([words[row][i-1] for row in range(1,i)])
        if words[i][len(string)]:
            results = getWords(string, words, i)

    # True if previous is true and this word in dictionary
    return results


def TestSuite():
    dictionary = ['quick', 'brown', 'the', 'fox']
    string = "thequickbrownfox"
    expected = ['the', 'quick', 'brown', 'fox']
    actual = get_sentence(dictionary, string)

    assert expected == actual, "{} == {}".format(expected, actual)

    print("Done")


if __name__ == "__main__":
    TestSuite()
