class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        student_pref = Counter(students)
        for sand in sandwiches:
            if student_pref[sand] > 0:
                student_pref[sand] -=1
            else:
                return sum(student_pref.values())
        return 0