# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
          head = ListNode(-1)
          current = head

          while list1 and list2: 
             if list1.val < list2.val:
                 current.next = list1
                 list1 = list1.next
             else:
                 current.next = list2
                 list2 = list2.next
             current = current.next

          current.next = list1 or list2
          return head.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
            if not lists:
                return None

            merged_list = lists[0]
            for i in range(1, len(lists)):
                merged_list = self.mergeTwoLists(merged_list, lists[i])
            
            return merged_list