#!/usr/bin/env python
# coding=utf-8
# https://github.com/allentofight/easy-cs/blob/main/%E7%AE%97%E6%B3%95/%E4%B8%80%E6%96%87%E5%AD%A6%E4%BC%9A%E9%80%92%E5%BD%92%E8%A7%A3%E9%A2%98.md
"""
细胞分裂 有一个细胞 每一个小时分裂一次，一次分裂一个子细胞，第三个小时后会死亡。
那么n个小时候有多少细胞？
"""
"""
a 状态: 细胞的初始态
b 状态: 细胞的幼年态
c 状态: 细胞的成熟态

"""

# 第 n 小时状态的细胞数
def aCell(n):
    if n==1:
        return 1
    return aCell(n-1) + bCell(n-1) + cCell(n-1)

# 第 n 小时 b 状态细胞数
def bCell(n):
    if n==1:
        return 0
    return aCell(n-1)

# 第 n 小时 c 状态细胞数
def cCell(n):
    if n==1 or n==2:
        return 0
    return bCell(n-1)

# 第 n 小时所有细胞
def allCells(n):
    return aCell(n) + bCell(n) + cCell(n)

if __name__ == '__main__':
    n = 20
    print(allCells(n))

