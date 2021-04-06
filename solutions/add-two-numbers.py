# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(list_):
    head = ListNode(0)
    p = head
    for i in list_:
        p.next = ListNode(i)
        p = p.next

    return head.next


def print_list(l):
    while l:
        print("{} {}".format(l, l.val))
        l = l.next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = curr = ListNode()
        carry = val = 0
        while carry or l1 or l2:
            val = carry
            if l1:
                l1, val = l1.next, l1.val + val
            if l2:
                l2, val = l2.next, l2.val + val

            carry, val = divmod(val, 10)
            curr.next = curr = ListNode(val)
        return head.next


if __name__ == '__main__':
    list_data = [2, 4, 3]
    list_data2 = [5, 6, 4]
    l = build_list(list_data)
    l2 = build_list(list_data2)
    s = Solution()
    h = s.addTwoNumbers(l, l2)
    print_list(h)
