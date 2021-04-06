#!/usr/bin/env python
# coding=utf-8
"""
给定 amount 金额和coins数组的硬币，
求凑成amount金额的钱，最少需要多少枚硬币
eg.
amount = 11
coins = [1,2,5]
输出 3 (5元 *2 + 1元 *1)
"""

def exchange(amount,coins):
    if amount ==0 :
        return 0
    if amount < 0:
        return -1
    result = 2**32
    for i in range(len(coins)):
        sub_min = exchange(amount - coins[i],coins)
        if sub_min == -1:
            continue
        result = min(sub_min+1,result)
    if result == 2**32:
        return -1
    return result

if __name__ == '__main__':
    amount = 11
    coins = [1,2,5]
    result = exchange(amount,coins)
    print("result: {}".format(result))
