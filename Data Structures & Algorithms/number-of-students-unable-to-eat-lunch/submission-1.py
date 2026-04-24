class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students) #number of students
        q = deque(students) #

        res = n
        for sand in sandwiches:
            cnt = 0
            while cnt < n and q[0] != sand:
                current = q.popleft()
                q.append(current)
                cnt +=1
            
            if q[0] == sand:
                q.popleft()
                res -= 1
            else:
                break
        return res