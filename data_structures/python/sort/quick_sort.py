#!/usr/bin/env python
# coding=utf-8
import random

def quick_sort(list_):
    if len(list_) < 2:
        return list_
    pivot = list_[0]
    small = [i for i in list_[1:] if i < pivot]
    great = [i for i in list_[1:] if i >= pivot]
    return quick_sort(small) + [pivot] + quick_sort(great)

if __name__ == '__main__':
    l = [random.randint(1,100) for x in range(10)]
    print(l)
    l = quick_sort(l)
    print(l)
