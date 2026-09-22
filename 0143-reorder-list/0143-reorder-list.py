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
    
    def reorderList(self, head: ListNode | None) -> None:
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            if fast.next.next is not None:    
                slow = slow.next
            fast = fast.next.next

        r = slow.next
        slow.next = None

        l = head
        r = self.reverseList(r)

        while l is not None and r is not None:
            temp = l.next
            temp2 = r.next
            l.next = r
            r.next = temp
            l = temp
            r = temp2
            