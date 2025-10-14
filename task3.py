#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    for num in range(10, 100):
        digit1 = num // 10
        digit2 = num % 10
        digit_sum = digit1 + digit2

        if num % digit_sum == 0:
            print(num)