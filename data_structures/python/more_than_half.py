#!/usr/bin/env python
# coding=utf-8
import random

def more_than_half(numbers):
    dict = {}
    for num in numbers:
        if num not in dict:
            dict[num] = 1
        else:
            dict[num] += 1
        if dict[num] > len(numbers) / 2:
            return num
    return 0

if __name__ == '__main__':
    numbers_ = [random.randint(1,7) for x in range(10)]
    print("numbers_ {}".format(numbers_))
    print(more_than_half(numbers_))
