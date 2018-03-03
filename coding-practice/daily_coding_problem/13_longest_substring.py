"""
    Given an integer k and a string s, find the length of the longest
    substring that contains at most k distinct characters.

    For example, given s = "abcba" and k = 2, the longest substring
    with k distinct characters is "bcb", so your function should return 3.
"""


def longest_substring(string, k):

    T = [[{"hash": dict(), "length": 0} for i in range(len(string))] for j in range(len(string))]
    max_length = 0

    for i in range(len(string)):
        for j in range(i, len(string)):
            letter = string[j]
            hsh = T[i][j-1]["hash"]
            T[i][j] = {"hash": dict(hsh), "length": (T[i][j-1]["length"] + 1 if hsh.get(letter) is None else T[i][j-1]["length"])}
            T[i][j]["hash"][letter] = True

            # Add the count for this set of strings, add length
            if len(hsh) > k:
                max_length = max(T[i][j]["length"], max_length)

    return max_length


def TestSuite():
    string = "abcba"
    k = 2
    output = 3
    actual = longest_substring(string, k)

    assert actual == output, "{} == {}".format(actual, output)

    print("Successfully completed")

if __name__ == "__main__":
    TestSuite()
