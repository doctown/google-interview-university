"""
    Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

    For example, given the string "([])[]({})", you should return true.

    Given the string "([)]" or "((()", you should return false.

([])

Time: O(n) | Space: O(n), could be done in constant space
"""


def well_balanced(string):
    match = {')': '(', '}': '{', ']': '['}
    stack = []

    for i in range(len(string)):
        ch = string[i] # ( -> [ -> ]

        if len(stack):
            peek = stack[len(stack) - 1]  # ( -> [
            if match.get(ch) == peek: # None == ( -> [ == [
                stack.pop()
            else:
                stack.append(ch) # ([ ->
        else:
            stack.append(ch) # ( ->

    return len(stack) == 0


def TestSuite():
    string = "([])[]({})"
    output = True
    assert well_balanced(string) == output, string

    string = "([)]"
    output = False
    assert well_balanced(string) == output, string

    string = "((()"
    output = False
    assert well_balanced(string) == output, string

    print("Done")


TestSuite()
