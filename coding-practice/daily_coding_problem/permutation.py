def perm(string, rem_string):
    if len(rem_string) == 0:
        print(string)
        return

        # acb abc
        # bac bca
        # cab cba

    for i in range(len(rem_string)):
        char = rem_string[i]
        left = rem_string[:i] + rem_string[i + 1:]
        perm(string + char, left)


def derangement(string, remainder, original_string):
    if len(remainder) == 0:
        print(string)
        return string

    for i in range(len(remainder)):
        char = remainder[i]

        if char != original_string[len(string)]:
            left = remainder[:i] + remainder[i + 1:]
            derangement(string + char, left, original_string)


# perm("", "abc")
derangement("", "abc", "abc")
