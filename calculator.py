class Calculator:
   def addition(self,*args):
        sum =args[0]
        for num in args[1:]:
          sum+=num
        return sum
   def subtraction(self,*args):
        sub=args[0]
        for num in args[1:]:
            sub-=num
        return sub
   def multiply(self,*args):
        multiple =args[0]
        for num in args[1:]:
            multiple*=num
        return multiple
   def divide(self,*args):
        if 0 in args[1:]:
            return {f"Error: Division by zero"}
        div = args[0]
        for num in args[1:]:
            div /= num
        return div
calculate = Calculator()

print("Addition:", calculate.addition(10, 5))                  
print("Subtraction:", calculate.subtraction(10, 5, 2))       
print("Multiplication:", calculate.multiply(2, 3, 4))    
print("Division:", calculate.divide(20, 2, 5))            
print("Division by zero:", calculate.divide(10, 0, 2))
