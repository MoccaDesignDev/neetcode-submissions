# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
         newarr =[]
          
         current = head
         while current:
           newarr.append(current.val)  # Store value in array
           current = current.next    # Move to next node
    
         newarr.reverse()
         
         head = ListNode(0)
         curr = head
         for val in newarr:
             curr.next = ListNode(val)
             curr = curr.next
         return head.next