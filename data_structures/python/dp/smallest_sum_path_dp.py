#!/usr/bin/env python
# coding=utf-8
triangle = [
    [2,0,0,0],
    [3,4,0,0],
    [6,5,7,0],
    [4,1,8,3]
]

def traverse():
    row = 4
    mini = triangle[row-1]
    i = row-2
    while i>0:
        for j in range(0,len(triangle[i]) - 1):
            mini[j] = triangle[i][j] + min(mini[j],mini[j+1])
        i -=1
    print(mini)
    return mini[0]

if __name__ == '__main__':
    mini_path_num = traverse()
    print("sum= {}".format(mini_path_num))
