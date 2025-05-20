 #Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        while curr:
            curr = curr.next
            count+=1
        pos = count - n
        curr = dummy
        
        
        for _ in range(pos):
            curr = curr.next

        # Skip the node
        curr.next = curr.next.next
        return dummy.next
