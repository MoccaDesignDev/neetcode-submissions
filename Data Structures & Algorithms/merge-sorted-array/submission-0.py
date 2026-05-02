class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        
        #verify the lenth of the array1 with valid element m, then compare the array availablity with n
        #if there's room in array, append the array2 value to array1
        #then sort array 1

       # for element in range(len(nums1)):
        #    if len(nums1) > m:
        #        for value in range(len(num2)):
                #        nums1.append(element)
         #   else:
          #      return "No room for merging"
          #  nums1.sort()
        #return nums1

        if len(nums1) >= m + n:
            for i in range(n):
                 nums1[m+i] = nums2[i]
        else:
            return "no room for merging"
        
        nums1.sort()

