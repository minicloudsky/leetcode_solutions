#!/usr/bin/env python
# coding=utf-8
"""
求三角形的最小路径和


"""
triangle = [
    [2,0,0,0],
    [3,4,0,0],
    [6,5,7,0],
    [4,1,8,3]
]

def traverse(i,j):
    # 总行数
    total_row = 4
    if i >= total_row -1:
        return 0
    left_sum = traverse(i+1,j) + triangle[i+1][j]
    right_sum = traverse(i+1,j+1) + triangle[i+1][j+1]
    return min(left_sum, right_sum)

if __name__ == '__main__':
    sum_ = traverse(0,0) + triangle[0][0]
    print("sum = {}".format(sum_))
