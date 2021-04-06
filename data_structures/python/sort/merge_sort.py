#!/usr/bin/env python
# coding=utf-8
import random

def merge_sort(list_):
    if len(list_) < 2:
        return list_
    mid = int(len(list_)/2)
    left = merge_sort(list_[:mid])
    right = merge_sort(list_[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
    result.extend(left)
    result.extend(right)
    return result

if __name__ == '__main__':
    l = [random.randint(1,100) for x in range(15)]
    print("Before sort: {}".format(l))
    l = merge_sort(l)
    print("After sort: {}".format(l))
