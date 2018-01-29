"""
    cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the
    first and last element of that pair. For example, car(cons(3, 4)) returns 3
    , and cdr(cons(3, 4)) returns 4.

    Given this implementation of cons:

    def cons(a, b):
       return lambda f : f(a, b)

       Implement car and cdr.
"""


def car(f):
    return f(lambda a, b: a)


def cdr(f):
    return f(lambda a, b: b)


def cons(a, b):
    return lambda f: f(a, b)


if __name__ == "__main__":
    print(car(cons(2, 3)))
    print(cdr(cons(3, 3)))
