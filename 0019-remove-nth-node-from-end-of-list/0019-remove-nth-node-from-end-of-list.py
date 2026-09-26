# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev

    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        head = self.reverseList(head)
        
        curr = head
        prev = None

        for i in range(n-1):
            prev = curr
            curr = curr.next

        if prev is None:
            head = curr.next
        else:
            prev.next = curr.next

        return self.reverseList(head)