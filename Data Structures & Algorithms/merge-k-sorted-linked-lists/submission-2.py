# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        hp= []

        for index, head, in enumerate(lists):
            if head:
                heapq.heappush(hp,(head.val,index,head))

        dummy = ListNode()
        current = dummy
        while hp:
            val, index, node = heapq.heappop(hp)
            current.next = node

            if node.next:
                heapq.heappush(hp,(node.next.val, index, node.next))
            
            current = current.next

        return dummy.next