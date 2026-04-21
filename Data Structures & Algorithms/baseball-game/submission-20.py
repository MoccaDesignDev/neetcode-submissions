class Solution:
    def calPoints(self, operations: List[str]) -> int:
      top=-1
      suma=0
      stack=[]

      for op in operations:

            if op =="+":
                top+=1
                stack.append(stack[top-1]+stack[top-2])
                suma+=stack[top]

            elif op =="D":
                top+=1
                stack.append(2* stack[top-1])
                suma+=stack[top]


            elif op=="C":
             suma-=stack.pop()
             top-=1


            else:
                top+=1
                stack.append(int(op))
                suma+=stack[top]


      return suma