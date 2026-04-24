class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts = [students.count(0), students.count(1)]
        
        for sand in sandwiches:
            if counts[sand] > 0:
                counts[sand] -= 1
            else:
                # If no student left wants this sandwich, the process stops
                break

        return counts[0] + counts[1]