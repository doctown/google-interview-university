from collections import namedtuple

Utxo = namedtuple('UTXO', ('time', 'value'))
PaymentRange = namedtuple('PaymentRange', ('value', 'start_time', 'end_time'))


def compare(payment_range):
    return (payment_range.value, payment_range.start_time - payment_range.end_time)


def find_range(utxos, x):
    best_range = max([check_range(utxos[idx + 1:], x - utxos[idx].value, utxos[idx].time, utxos[idx].time) for idx in range(len(utxos))], key=compare)
    return [best_range.start_time, best_range.end_time]


def check_range(utxos, x, start_time, end_time):
    if x <= 0:
        return PaymentRange(x, start_time, end_time)
    if len(utxos) == 0:
        return PaymentRange(float('-inf'), float('-inf'), float('-inf'))
    return max([check_range(utxos[idx + 1:], x - utxos[idx].value, start_time, utxos[idx].time) for idx in range(len(utxos))], key=compare)


def TestSuite():
    # 1 transaction
    utxos = [Utxo(100, 5)]
    x = 5
    output = [100, 100]
    actual = find_range(utxos, x)
    assert output == actual, "{} == {}".format(output, actual)

    # Multiple transactions, exact amount available by multiple transactions
    utxos = [Utxo(100, 5), Utxo(101, 10), Utxo(102, 2), Utxo(103, 3)]
    x = 8
    output = [100, 103]
    actual = find_range(utxos, x)
    assert output == actual, "{} == {}".format(output, actual)

    utxos = [Utxo(100, 3), Utxo(101, 2), Utxo(102, 6), Utxo(103, 3)]
    x = 8
    output = [101, 102]
    actual = find_range(utxos, x)
    assert output == actual, "{} == {}".format(output, actual)

    # Multiple transactions, exact amount available by single and multiple transactions, chooses smallest time frame
    utxos = [Utxo(100, 5), Utxo(101, 10), Utxo(102, 2), Utxo(103, 3), Utxo(104, 8)]
    x = 8
    output = [104, 104]
    actual = find_range(utxos, x)
    assert output == actual, "{} == {}".format(output, actual)

    # Multiple transactions, nearest amount available by single and multiple transactions
    utxos = [Utxo(100, 5), Utxo(101, 10), Utxo(102, 2), Utxo(103, 3)]
    x = 9
    output = [101, 101]
    actual = find_range(utxos, x)
    assert output == actual, "{} == {}".format(output, actual)

    # Cannot make target amount with current transactions
    utxos = [Utxo(100, 3), Utxo(101, 2), Utxo(102, 6), Utxo(103, 3)]
    x = 20
    output = [float('-inf'), float('-inf')]
    actual = find_range(utxos, x)
    assert output == actual, "{} == {}".format(output, actual)

    print("Done")


TestSuite()
