"""
Problem:  Write a function fib() that a takes an integer nnn and returns the nnnth fibonacci number.
"""
memo = {}
def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        if memo.get(n -1) is None:
            memo[n - 1] = fib(n - 1)
        if memo.get(n -2) is None:
            memo[n - 2] = fib(n - 2)
        return memo[n - 2] + memo[n -1]

def TestSuite():
    print("fib({0}) => {1}".format(0, fib(0)))
    assert(fib(0) == 0)

    print("fib({0}) => {1}".format(1, fib(1)))
    assert(fib(1)==  1)

    print("fib({0}) => {1}".format(2, fib(2)))
    assert(fib(2)==  1)

    print("fib({0}) => {1}".format(3, fib(2)))
    assert(fib(3)==  2)

    print("fib({0}) => {1}".format(4, fib(4)))
    assert(fib(4)==  3)


    print("fib({0}) => {1}".format(113, fib(113)))
    assert(fib(113) ==  184551825793033096366333)

TestSuite()
