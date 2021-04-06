#!/usr/bin/env python
# coding=utf-8

hash_table = {}

def fibonacci(n):
    if n==1:
        return 1
    if n==2:
        return 1
    if hash_table.get(n):
        return hash_table.get(n)
    res = fibonacci(n-1) + fibonacci(n-2)
    hash_table[n] = res
    return res
    


if __name__ == '__main__':
    n = 5
    print(fibonacci(n))
