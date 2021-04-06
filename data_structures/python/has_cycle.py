#!/usr/bin/env python
# coding=utf-8

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def has_cycle(head):
    if head == None or head.next == None:
        return False
    node1 = head
    node2 = head.next
    while node1 != node2:
        if node2 == None or node2.next == None:
            return False
        node1 = node1.next
        node2 = node2.next
    return True



def build_list(arr):
    head = ListNode(0)
    p = head
    for n in arr:
        p.next = ListNode(n)
        p = p.next
    return head.next

if __name__ == '__main__':
    list_ = [1,2,3,4,5]
    l = build_list(list)

