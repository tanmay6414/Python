class Node:
    ''' class to create a node element to be used in Stack'''
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_next(self, node):
        self.next = node

class Stack:
    ''' class to create a Stack (follows 'Last In First Out', i.e. LIFO) using Node objects as elements'''
    def __init__(self):
        self.top = None                                                      # To maintain top element in the stack
        print("\n\t","*"*25,"Stack created","*"*25)

    def push(self, newdata):
        ''' method to insert elements in the stack from top'''
        newNode = Node(newdata)
        if self.is_empty():
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        #print(newNode.data)

    def pop(self):
        ''' method to remove top element from the stack'''
        if self.is_empty():
            return ("No element to pop!!!")
        else:
            popped = self.top
            self.top = self.top.next
            return (str(popped.data))
        
    def is_empty(self):
        ''' method that returns True if stack is empty, False otherwise'''
        return self.top == None
    
    def Top(self):
        ''' method to peek the top element in the stack'''
        return ("Top is: " + str(self.top.data) + "\n") if self.top else ("Top is None")
        
    def __str__(self):
        ''' overloading the print method to print the stack in proper format'''
        stack = ''
        curr = self.top
        if self.is_empty():
            return "\tStack is empty!!!"
        else:
            while curr:
                stack += '\t| ' + str(curr.data) + ' |\n'
                curr = curr.next
        stack = "\nSTACK is:\n -->" + stack + "\t------"
        return stack


def main():
    s = Stack()

    expr = input("Enter the expression: ")
    ops = ['+', '-', '*', '/', '^']

    for ch in expr[::-1]:
        if ch not in ops:
            s.push(ch)
        else:
            if ch == '+':
                temp = str(s.pop()) + '+' + str(s.pop())
            elif ch == '-':
                temp = str(s.pop()) + '-' + str(s.pop())
            elif ch == '*':
                temp = str(s.pop()) + '*' + str(s.pop())
            elif ch == '/':
                temp = str(s.pop()) + '/' + str(s.pop())
            elif ch == '/':
                temp = str(s.pop()) + '/' + str(s.pop())
            temp = "(" + temp + ")"
            s.push(temp)

        print(s)


if __name__ == "__main__":
    main()


'''
OUTPUT

         ************************* Stack created *************************
Enter the expression: *+AB-CD

STACK is:
 -->    | D |
        ------

STACK is:
 -->    | C |
        | D |
        ------

STACK is:
 -->    | (C-D) |
        ------

STACK is:
 -->    | B |
        | (C-D) |
        ------

STACK is:
 -->    | A |
        | B |
        | (C-D) |
        ------

STACK is:
 -->    | (A+B) |
        | (C-D) |
        ------

STACK is:
 -->    | ((A+B)*(C-D)) |
        ------
'''
