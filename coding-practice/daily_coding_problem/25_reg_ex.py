"""
    Implement regular expression matching with the following special characters:

• . (period) which matches any single character
• * (asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.

Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.

  "" c h a
""
.    T F F
*    F T F
a    F F T
"""


import re


def regex(string, match):
    T = [[False] * (len(string) + 1) for _ in range(len(match) + 1)]

    for reg_idx in range(len(match) + 1):
        T[0][0] = True
        for str_idx in range(len(string) + 1):
            str_char = string[str_idx - 1]
            reg_char = match[reg_idx - 1]
            if reg_char == '.' or str_char == reg_char:
                T[reg_idx][str_idx] = T[reg_idx - 1][str_idx - 1]
            elif reg_char == '*':
                # https://www.youtube.com/watch?v=l3hda49XcDE
                T[reg_idx][str_idx] = (T[reg_idx][str_idx - 1] if match[reg_idx - 2] == '.' or str_char == match[reg_idx - 2] else False) or T[reg_idx - 2][str_idx]

                """
                # do something here
                char_before_star_idx = match[:reg_idx].rfind('*')
                char_before_star = match[char_before_star_idx - 1] if char_before_star_idx else ''
                works but not on empty string
                if char_before_star == '':
                    T[reg_idx][str_idx] = T[reg_idx - 1][str_idx - 1]
                elif char_before_star == '.' or char_before_star == str_char:
                    T[reg_idx][str_idx] = T[reg_idx - 1][str_idx - 1] or T[reg_idx][str_idx - 1]
                elif:
                    # empty
                else:
                    T[reg_idx][str_idx] = False
                """

            else:
                T[reg_idx][str_idx] = False

    return T[len(match)][len(string)]


def TestSuite():
    string = "ray"
    match = "ra."
    actual = regex(string, match)
    output = True

    assert actual == output, "{} == {} is {} but should be {}".format(string, match, actual, output)

    string = "raymond"
    match = "ra."
    actual = regex(string, match)
    output = False

    assert actual == output, "{} == {} is {} but should be {}".format(string, match, actual, output)

    string = "chat"
    match = ".*at"
    actual = regex(string, match)
    output = True

    assert actual == output, "{} == {} is {} but should be {}".format(string, match, actual, output)

    string = "chats"
    match = ".*at"
    actual = regex(string, match)
    output = False

    assert actual == output, "{} == {} is {} but should be {}".format(string, match, actual, output)

    string = "chatsrrrrrrrr"
    match = ".*at.r*"
    actual = regex(string, match)
    output = True

    assert actual == output, "{} == {} is {} but should be {}".format(string, match, actual, output)

    print("Done")

TestSuite()
