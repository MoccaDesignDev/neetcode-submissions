import heapq
from typing import List


def get_min_element(arr: List[int]) -> int:
  

  min_1 = heapq.nsmallest(1, arr)
  # this is wrong, it's returning the whole list return min_1 
  # the following is right just returning the value at index 0
  return min_1[0]


def get_min_4_elements(arr: List[int]) -> List[int]:
    # Return elements in *increasing* order
    
  return heapq.nsmallest(4, arr)

def get_min_2_elements(arr: List[int]) -> List[int]:
    # Return elements in *decreasing* order
   # this is wrong, use slicing to reverse the orde 
    #return heapq.nsmallest(2, arr)
    #slicing and -1 to reverse the order
    return heapq.nsmallest(2, arr)[::-1]


# do not modify below this line
print(get_min_element([1, 2, 3]))
print(get_min_element([3, 2, 1, 4, 6, 2]))
print(get_min_element([1, 9, 7, 3, 2, 1, 4, 6, 2]))

print(get_min_4_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_4_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_4_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

print(get_min_2_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_2_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_2_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

