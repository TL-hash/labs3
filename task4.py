#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys

EPS = 1e-10

if __name__ == '__main__':
    x = float(input("Value of x? "))
    n = int(input("Value of n? "))
    if n < 0:
        print("Illegal value of n", file=sys.stderr)
        exit(1)

    a = 1 / math.factorial(n)
    S, k = a, 0

    while math.fabs(a) > EPS:
        a *= (x**2 / 4) / ((k + 1)*(k + 1 + n))
        S += a
        k += 1

    res = (x / 2) ** n * S

    print(f"I{n}({x}) = {res}")