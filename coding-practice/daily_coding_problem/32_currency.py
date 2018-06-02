"""
Suppose you are given a table of currency exchange rates, represented as a 2D array. Determine whether there is a possible arbitrage: that is, whether there is some sequence of trades you can make, starting with some amount A of any currency, so that you can end up with some amount greater than A of that currency.

There are no transaction costs and you can trade fractional quantities.

    USA    MEX    BTC
USA  1      2      4
MEX .5      1      2
BTC .25   .125     1

    USA    MEX    BTC
USA  1      2      4
MEX  .5     1      2
BTC  .25   .125    1
"""


def arbitrage(exchange_rates, start_row=0):
    found = False

    for dest_row in range(len(exchange_rates[0])):
        found |= arbitrage_helper(exchange_rates, 0, dest_row, exchange_rates[0][dest_row], set([(0, dest_row)]))

    return found


def arbitrage_helper(exchange_rates, start_row, dest_row, cum_val, visited=set()):
    if dest_row == start_row:
        return cum_val > 1
    else:
        found = False

        for visit_col in range(len(exchange_rates[dest_row])):
            if (dest_row, visit_col) not in visited:
                new_set = set(visited)
                new_set.add((dest_row, visit_col))
                found |= arbitrage_helper(exchange_rates, start_row, visit_col, cum_val * exchange_rates[dest_row][visit_col], new_set)
        return found


def TestSuite():
    exchange_rates = [[1, .75, 4],
                      [.5, 1, 2],
                      [.7, .25, 1]]
    expected = True
    actual = arbitrage(exchange_rates)

    assert actual == expected, "{} == {}".format(actual, expected)

    exchange_rates = [[1, 2, 4],
                      [.5, 1, 2],
                      [.25, .5, 1]]
    expected = False
    actual = arbitrage(exchange_rates)

    assert actual == expected, "{} == {}".format(actual, expected)

    print("Done")


TestSuite()
