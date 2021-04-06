#!/usr/bin/env python
# coding=utf-8

def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    res = 0
    pre = 1
    next_ = 1
    for i in range(3,n+1):
        res = pre + next_
        pre = next_
        next_ = res
    return res

if __name__ == '__main__':
    n = 5
    print(fib(n))
