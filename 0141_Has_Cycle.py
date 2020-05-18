# Definition for single-linked list
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        fast, slow = head, head
        while fast and fast.next: # 用来判断链表是否为空，和是否检索到末尾了
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                return True
        return False
