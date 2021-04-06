#!/usr/bin/env python
# coding=utf-8
import random

def bubble_sort(list_):
    for i in range(0,len(list_)-1):
        for j in range(i,len(list_)):
            if list_[i] > list_[j]:
                list_[i], list_[j] = list_[j], list_[i]
    return list_

if __name__ == '__main__':
    l = [random.randint(1,100) for x in range(10)]
    print(l)
    l = bubble_sort(l)
    print(l)
