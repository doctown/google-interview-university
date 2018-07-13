def min_product(first_num, second_num):
    smaller = first_num if first_num < second_num else second_num
    bigger = first_num if first_num > second_num else second_num

    memo = {}
    return min_product_memo(smaller, bigger, memo)


def min_product_memo(smaller, bigger, memo):
    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger
    elif memo.get(smaller) is not None:
        return memo[smaller]
    s = smaller >> 1
    side1 = min_product_memo(s, bigger, memo)
    side2 = side1
    if smaller % 2 == 1:
        side2 = min_product_memo(smaller - s, bigger, memo)
    print(side1 + side2)
    memo[smaller] = side1 + side2

    return memo[smaller]


print(min_product(4, 23))

