class Evaluate: 
    def __init__(self, capacity): 
        self.top = -1
        self.capacity = capacity 
        self.array = [] 

    def isEmpty(self): 
        return True if self.top == -1 else False
      
    def peek(self): 
        return self.array[-1] 
      
    def pop(self): 
        if not self.isEmpty(): 
            self.top -= 1
            return self.array.pop() 
        else: 
            return "$"
      
    def push(self, op): 
        self.top += 1
        self.array.append(op)  
  
    def evaluatePostfix(self, exp): 
        # Iterate over the expression for conversion 
        for i in exp: 
            # If the scanned character is an operand 
            # (number here) push it to the stack 
            if i.isdigit(): 
                self.push(i) 
            # If the scanned character is an operator, 
            # pop two elements from stack and apply it. 
            else: 
                val1 = self.pop() 
                val2 = self.pop() 
                self.push(str(eval(val2 + i + val1))) 
  
        return int(self.pop()) 
                  
    def evaluatePrefix(self, exp): 
        # Iterate over the expression for conversion 
        for i in exp[::-1]: 
            # If the scanned character is an operand 
            # (number here) push it to the stack 
            if i.isdigit(): 
                self.push(i) 
            # If the scanned character is an operator, 
            # pop two elements from stack and apply it. 
            else: 
                val1 = self.pop() 
                val2 = self.pop() 
                self.push(str(eval(val1 + i + val2))) 
  
        return int(self.pop()) 
  
              

#exp = "45*9+2-"
exp = input("Enter Postfix expression: ")
obj = Evaluate(len(exp)) 
print ("Postfix evaluation: %d"%(obj.evaluatePostfix(exp)))

#exp = "-+*4592"
exp = input("Enter Prefix expression: ")
obj = Evaluate(len(exp)) 
print ("Prefix evaluation: %d"%(obj.evaluatePrefix(exp)))