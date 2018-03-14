"""
    Suppose we represent our file system by a string in the following manner:

    The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
        dir
            subdir1
            subdir2
                file.ext

    The directory dir contains an empty sub-directory subdir1 and a
    sub-directory subdir2 containing a file file.ext.

    The string
    "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

    dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext

    The directory dir contains two sub-directories subdir1 and subdir2.
    subdir1 contains a file file1.ext and an empty second-level sub-directory
    subsubdir1. subdir2 contains a second-level sub-directory subsubdir2
    containing a file file2.ext.

    We are interested in finding the longest (number of characters)
    absolute path to a file within our file system. For example, in the second
    example above, the longest absolute path is
    "dir/subdir2/subsubdir2/file2.ext",
    and its length is 32 (not including the double quotes).

    Given a string representing the file system in the above format,
    return the length of the longest absolute path to a file in the abstracted
    file system. If there is no file in the system, return 0.

    Note:
    The name of a file contains at least a period and an extension.
    The name of a directory or sub-directory will not contain a period.
"""


def longest_file_path(path):
    count = 0
    paths = {}
    key = ""
    total = 0
    i = 0

    while i <= len(path):
        if i == len(path):
            assign_key(paths, key, count)
            i += 1
        else:
            char = path[i]

            if char == "\n":
                assign_key(paths, key, count)
                i, key = get_symbol(path, i)
                count = 0
            else:
                count += 1
                i += 1

    for key, value in paths.items():
        total += paths[key]

    return total


def assign_key(paths, key, count):
    if paths.get(key):
        paths[key] = max(paths[key], count)
    else:
        paths[key] = count


def get_symbol(path, i):
    key = ""
    while (path[i] == "\n" or path[i] == "\t") and i < len(path):
        key += path[i: i+1]
        i += 1

    return i, key


def testSuite():
    path = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    expected = 18
    actual = longest_file_path(path)
    assert expected == actual, "{} == {}".format(expected, actual)

    path = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    expected = 32
    actual = longest_file_path(path)
    assert expected == actual, "{} == {}".format(expected, actual)


if __name__ == "__main__":
    testSuite()
