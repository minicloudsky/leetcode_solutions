#!/usr/bin/env python
# coding=utf-8

triangle = [
    [2,0,0,0],
    [3,4,0,0],
    [6,5,7,0],
    [4,1,8,3]
]
map_ = {}

def traverse(i,j):
    key = str(i) + "" + str(j)
    if map_.get(key):
        return map_.get(key)
    total_row = 4 # 总行数
    if i >= total_row -1:
        return 0
    # 往左下节点走
    left_sum = traverse(i+1,j) + triangle[i+1][j]
    # 往右下节点走
    right_sum = traverse(i+1,j+1) + triangle[i+1][j+1]
    # 记录每个节点往左和往右遍历的路径和最小值
    res = min(left_sum, right_sum)
    map_[key] = res
    return res

if __name__ == '__main__':
    print(__name__)
    sum_ = traverse(0,0) + triangle[0][0]
    print("sum = %s" %(sum_))
