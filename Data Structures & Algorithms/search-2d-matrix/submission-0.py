class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #first by determining which array to search the target
        #we know that the array are in ascending order, which mean array 3 is bigger than array 2 and 1
        #we can first by targeting the middle array's middle data, if the target is 
        rows = len(matrix)
        cols = len(matrix[0])
        # total elements if flattened
        total_elements = rows * cols

        L, R = 0, total_elements - 1
        while L <= R:
            mid = (L + R) // 2
            #map a 1D index 'mid' to 2D
            r = mid // cols
            c = mid % cols
            val = matrix[r][c]

            if target > val:
                L = mid + 1
            elif target < val:
                R = mid - 1
            else:
                return True

        return False