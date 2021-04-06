#!/usr/bin/env python
# coding=utf-8
import random

def shell_sort(list_):
    i, j = 0, 0
    gap = int(len(list_) / 2)
    while gap > 0:
        for i in range(gap, len(list_)):
            temp = list_[i]
            j = i
            while j >= gap:
                if temp < list_[j - gap]:
                    list_[j] = list_[j - gap]
                else:
                    break
                j -= gap
            list_[j] = temp
        gap  = int(gap / 2)
    return list_

if __name__ == '__main__':
    data = [random.randint(1,100) for x in range(10)]
    print("before sort: {}".format(data))
    data = shell_sort(data)
    print("after sort: {}".format(data))


