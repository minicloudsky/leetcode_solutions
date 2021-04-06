#!/usr/bin/env python
# coding=utf-8
import random

def insert_sort(relist):
    len_ = len(relist)
    for i in range(1,len_):
        for j in range(i):
            if relist[i] < relist[j]:
                relist.insert(j,relist[i])
                relist.pop(i+1)
                break
    return relist

if __name__ == '__main__':
    l = [random.randint(1,100) for x in range(10)]
    print(l)
    l = insert_sort(l)
    print(l)
