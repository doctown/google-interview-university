"""
    Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count
    the number of ways it can be decoded.

    For example, the message '111' would give 3, since it could be decoded as '
    aaa, 'ka', and 'ak'.
"""


decode = {
        "1": "a",
        "2": "b",
        "3": "c",
        "4": "d",
        "5": "e",
        "6": "f",
        "7": "g",
        "8": "h",
        "9": "i",
        "10": "j",
        "11": "k",
        "12": "l",
        "13": "m",
        "14": "n",
        "15": "o",
        "16": "p",
        "17": "q",
        "18": "r",
        "19": "s",
        "20": "t",
        "21": "u",
        "22": "v",
        "23": "w",
        "24": "x",
        "25": "y",
        "26": "z",
        }


def decode_count(code):
    if len(code) == 0:
        return 1
    else:
        one_letter = decode_count(code[1:])
        two_letter = 0
        if len(code) > 1:
            two_letter = decode_count(code[2:]) if decode.get((code[:2])) else 0
        return one_letter + two_letter


def TestSuite():
    code = "111"
    output = 3
    actual = decode_count(code)

    assert output == actual, "{} == {}".format(output, actual)

    code = "1"
    output = 1
    actual = decode_count(code)

    assert output == actual, "{} == {}".format(output, actual)

    code = "483"
    output = 1
    actual = decode_count(code)

    assert output == actual, "{} == {}".format(output, actual)

    print("Successfully completed")


TestSuite()
