# -*- coding: utf-8 -*-

import math
from collections import Counter
from decimal import Decimal, getcontext

getcontext().prec = 1000

def expected_sum(a, k):
    """
    Work wrong with k>nunique(a)
    112 and 121 same for func, although in right way ex(112) = 3 and ex(121) = 5
    """
    count = Counter(a)

    ex = 0
    for num, freq in count.items():
        if (len(a) - freq) <= 0:
            prob = 1
        else:
            value_decimal = Decimal(k * math.log((len(a) - freq) / len(a)))
            result_decimal = Decimal.exp(value_decimal)
            prob = 1 - result_decimal
        ex += num * prob

    return Decimal(ex)

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')

    a = list(map(int, data[0].split(' ')))
    k = int(data[1])

    result = expected_sum(a, k)
    print(f"{result:.100f}")

if __name__ == "__main__":
    main()