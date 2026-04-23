# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        self.head = ListNode(-1)
    
        current = self.head  #we start with the dummy head, and from there iterate through both list
                              #while, we also compare the value in the node to arrange the ascending order 
                              #of the list, and rearrange its pointers, then set the last node tail point to null
        
        while list1 and list2:
             if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
             else:
                current.next = list2
                list2 = list2.next
             current = current.next
        
        current.next = list1 or list2
        return self.head.next