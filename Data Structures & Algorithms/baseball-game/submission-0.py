class Solution:
    def calPoints(self, operations: List[str]) -> int:
        newstack =[]
        for i in range(len(operations)):
            
            if operations[i] == "+":
                next_score = newstack[-1] + newstack[-2]
                newstack.append(next_score)
            elif operations[i] == "D":
                 next_score = newstack[-1] * 2
                 newstack.append(next_score)

            elif operations[i] == "C":
                 newstack.pop()
            else:
                 next_score = int(operations[i])
                 newstack.append(next_score)
        return sum(newstack)
