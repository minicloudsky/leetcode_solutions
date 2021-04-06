#!/usr/bin/env python
# coding=utf-8
class ListNode:
    def __init__(self,val):
        self.next = None
        self.val = val

def build_linkedlist(list_):
    # head 用来记录头结点位置
    head = ListNode(0)
    # p 用来遍历
    p = head
    for val in list_:
        p.next = ListNode(val)
        p = p.next
    # 因为头节点是0，因此构造的链表真正的头结点是 head.next
    return head.next

def delete_by_val(l,val):
    pass

def delete_by_index(l,index):
    pass

def insert(l,val,position):
    pass

def reverse_linkedlist(l):
    pass

def print_linkedlist(l):
    while l!=None:
        print("node: {},value: {},next:{}".format(l,l.val,l.next))
        l = l.next

if __name__ == '__main__':
    list_ = [1,2,3,4,5]
    l = build_linkedlist(list_)
    print_linkedlist(l)
