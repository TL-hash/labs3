#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys

if __name__ == '__main__':
    a = float(input("Value of a? "))
    b = float(input("Value of b? "))
    c = float(input("Value of c? "))
    if a == 0:
        print("Illegal value of a", file=sys.stderr)
        exit(1)

 #Делаем замену в уравнении x^2 = y и решаем относительно у

    D = b * b - 4 * a * c

    if D < 0:
        print("Действительных корней нет")
    elif D == 0:
        y = -b / (2 * a)
        if y < 0:
            print("Действительных корней нет")
        else:
            x1 = math.sqrt(y)
            x2 = -math.sqrt(y)
            print(f"x1 = {x1}")
            print(f"x2 = {x2}")
    else:
        y1 = (-b + math.sqrt(D)) / (2 * a)
        y2 = (-b - math.sqrt(D)) / (2 * a)

        if y1 >= 0 and y2 >= 0:
            x1 = math.sqrt(y1)
            x2 = -math.sqrt(y1)
            x3 = math.sqrt(y2)
            x4 = -math.sqrt(y2)
            print(f"x1 = {x1}")
            print(f"x2 = {x2}")
            print(f"x3 = {x3}")
            print(f"x4 = {x4}")
        elif y1 >= 0:
            x1 = math.sqrt(y1)
            x2 = -math.sqrt(y1)
            print(f"x1 = {x1}")
            print(f"x2 = {x2}")
        elif y2 >= 0:
            x1 = math.sqrt(y2)
            x2 = -math.sqrt(y2)
            print(f"x1 = {x1}")
            print(f"x2 = {x2}")
        else:
            print("Действительных корней нет")