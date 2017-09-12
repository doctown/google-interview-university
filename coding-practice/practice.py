"""
    Given two strings s and t, determine if they are isomorphic.

    Two strings are isomorphic if the characters in s can be replaced to get t.

    All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

    For example,
    Given "egg", "add", return true.
    e -> a : 1

    g -> d : 1

    2 - g
    1 - e
    -----
    3

    2 - d
    1 - a
    -----
    3

    {
        1: 1
        2: 1
    }

    aadd
    ccbb
    addc
    eefg

    2: 0

    Given "foo", "bar", return false.
    1 - f
    2 - o
    -----
    3

    1 - b
    1 - a
    1 - r
    -----
    3

    Given "paper", "title", return true.

    Given "dog" "dog", return true.
"""
# input: empty string, string
# output:
# constraint: O(N)
# edge cases: ??

def iso(str1, str2):
    if (len(str1) != len(str2)):
        return False

    isIso = True
    str1Hash = {}

    #   hash of the letters of str1
    for i in range(len(str1)):
        letter1 = str1[i]
        letter2 = str2[i]

        retrievedLetter = str1Hash.get(letter1)

        if retrievedLetter:
            if retrievedLetter != letter2:
                isIso = False
        else:
            str1Hash[letter1] = letter2

    return isIso

def testRun():
    str1 = "egg"
    str2 = "add"
    result = iso(str1, str2)
    print("original: {0} {1} result: {2}".format(str1, str2, result))
    assert(result == True)

    str1 = "foo"
    str2 = "bar"
    result = iso(str1, str2)
    print("original: {0} {1} result: {2}".format(str1, str2, result))
    assert(result == False)

if __name__ == "__main__":
    testRun()
