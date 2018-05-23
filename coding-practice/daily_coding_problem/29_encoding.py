"""
Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.

"""


# O(n)/O(n)
def encode(string):
    cur_char = string[0]
    cur_index = 0
    code = ''

    for i in range(1, len(string)):
        ch = string[i]
        if cur_char != ch or i == len(string) - 1:
            code += str(i - cur_index) + cur_char if i != len(string) - 1 else str(i - cur_index + 1) + cur_char
            cur_index = i
            cur_char = ch
    return code


def decode(string):
    num = 0
    code = ''

    for ch in string:
        while num > 0:
            code += ch
            num -= 1

        if ch.isdigit():
            num = int(ch)

    return code


def TestSuite():
    string = "AAAABBBCCDAA"
    actual = encode(string)
    output = "4A3B2C1D2A"
    assert actual == output, "{} == {}".format(actual, output)

    actual = decode(actual)
    assert actual == string, "{} == {}".format(actual, string)

    print("Done")

TestSuite()

