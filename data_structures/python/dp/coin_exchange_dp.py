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
    """初始化每个值为 amount+1,这样当最终求得的 dp[amount]
    为 amount+1时候，说明无解.
    dp数组表示 i 元钱最少需要 dp[i]个硬币
    """    
    dp = [amount+1  for x in range(amount+1)]
    
    # 0 硬币本来就没有，所以设置成 0
    dp[0] = 0
    for i in range(amount+1):
        for j in range(len(coins)):
            # i 是金额，coins[i] 是硬币，当金额比当前硬币面值小，肯定是换不了的
            if i >=coins[j]:
                dp[i] = min(dp[i - coins[j]] + 1,dp[i])
    if dp[amount] == amount+1:
        return -1
    return dp[amount]
    
if __name__ == '__main__':
    amount = 1111
    coins = [1,2,5]
    result = exchange(amount,coins)
    print("result: {}".format(result))
