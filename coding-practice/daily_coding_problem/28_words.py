"""
    Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line. There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly

"""


def combine(words, spaces):
    per_word_space = spaces // (len(words) - 1)
    first_word_space = per_word_space + (spaces - ((len(words) - 1) * per_word_space))
    spaced_words = words.pop(0) + ' ' * first_word_space
    while words:
        if len(words) == 1:
            spaced_words += words.pop()
        else:
            spaced_words += words.pop(0) + ' ' * per_word_space
    return spaced_words


def combine_words(words, k=1):
    # count each word in an array
    count = []
    results = []
    for word in words:
        count.append(len(word))

    # determine count under k
    total_letters = 0
    start = 0
    for i in range(len(words)):
# will need to subtract number of words
        if total_letters + count[i] < k - (i - start) and i < len(words) - 1:
            total_letters += count[i]
        elif i == len(words) - 1:
            total_letters += count[i]
            results.append(combine(words[start:], k - total_letters))
        else:
            results.append(combine(words[start:i], k - total_letters))
            # reset total count and start
            total_letters = count[i]
            start = i
    return results


def TestSuite():
    words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    output = ["the  quick brown", "fox  jumps  over", "the   lazy   dog"]
    k = 16
    actual = combine_words(words, k)
    assert output == actual, "{} == {}".format(output, actual)


TestSuite()
