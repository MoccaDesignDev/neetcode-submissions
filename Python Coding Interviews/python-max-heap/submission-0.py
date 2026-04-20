import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    heapq.heapify(nums)
    max_heap=[]
    top = []
    for num in nums:
      heapq.heappush(max_heap, -num)
    return [-heapq.heappop(max_heap) for _ in range(len(nums))]
   # while max_heap:
    #  top.append(-heapq.heappop(max_heap))
    #return top



# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
