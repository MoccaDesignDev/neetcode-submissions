class Solution:
    def calPoints(self, operations: List[str]) -> int:
        newstack=[]
        result = 0 
        for op in operations:
            if op =="+":
                result += newstack[-1] + newstack[-2]
                newstack.append(newstack[-1] + newstack[-2])
            elif op =="D":
                result += (2*newstack[-1])
                newstack.append(2*newstack[-1])
            elif op =="C":
                result -= newstack.pop()
            else:
                result += int(op)
                newstack.append(int(op))
        return result