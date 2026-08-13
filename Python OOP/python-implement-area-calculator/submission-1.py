import math

class AreaCalc:
    # TODO: Implement calculate method
   # def calculate(self, arg1: float, arg2: float = None)->float:
    #    area = 0
     #   if arg2 == None:
      #      area = math.pi *(arg1**2)
       #     return round(area, 2)
        #else:
         #   area = arg1 * arg2
          #  return area
    

   def calculate(self, *args):
        if len(args) ==1:
            return round(math.pi *args[0]**2, 2)
        elif len(args)==2:
            return args[0] * args[1]

# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
