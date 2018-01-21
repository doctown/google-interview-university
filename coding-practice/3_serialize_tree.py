"""
    This problem was asked by Google.

    Given the root to a binary tree, implement serialize(root), which
    serializes the tree into a string, and deserialize(s), which deserializes
    the string back into the tree.

    If you liked this problem, feel free to forward it along! If you got here
    from a forwarded email, you can sign up for Daily Coding Problem here. As
    always, shoot us an email if there's anything we can help with!
"""


class Tree:
    def __init__(self):
        self.root = []

    def insert_node(self, value):
        self.root.append(value)

    def print_string(self):
        return "".join(self.root)


def tree_string(element):
    if type(element) == str:
        return convert_string(element)
    else:
        return convert_tree(element)


def convert_string(string):
    tree = Tree()
    [tree.insert_node(i) for i in string]

    return tree


def convert_tree(tree):
    return tree.print_string()


if __name__ == "__main__":
    string = "This is a string"
    tree = tree_string(string)

    print(tree.root)

    print(tree_string(tree))
