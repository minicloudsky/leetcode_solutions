#!/usr/bin/env python
# coding=utf-8

class ListNode:
    def __init__(self,x):
        self.next = None
        self.val = x
def build_list(arr):
    head = ListNode(0)
    p = head
    for n in arr:
        p.next = ListNode(n)
        p = p.next
    return head.next
def print_list(head):
    while head:
        print("{} {}".format(head, head.val))
        head = head.next
def reverse_list(head):
    pre = None
    cur = head
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return pre

if __name__ == '__main__':
    list_ = [x for x in range(1,8)]
    l = build_list(list_)
    print("before reverse: ")
    print_list(l)
    l = reverse_list(l)
    print("after reverse: ")
    print_list(l)
