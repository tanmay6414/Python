


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


# In[2]:


class Stack:
    ''' class to create a Stack (follows 'Last In First Out', i.e. LIFO) using Node objects as elements'''
    def __init__(self):
        self.top = None                                                      # To maintain top element in the stack
        print("Stack created")

    def push(self, newdata):
        ''' method to insert elements in the stack from top'''
        newNode = Node(newdata)
        if self.is_empty():
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        print("+Pushed: ", newNode.data)

    def pop(self):
        ''' method to remove top element from the stack'''
        if self.is_empty():
            return ("No element to pop!!!")
        else:
            popped = self.top
            self.top = self.top.next
            return ("-Popped: " + str(popped.data))
        
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


# In[3]:


def main():
    stack_2 = Stack()
    
    while True:
        print("*"*35, "Menu", "*"*35)
        print("\t1. Push element into stack \n\t2. Display stack \n\t3. Pop element from stack \n\t4. Default test cases \n\t5. Show max element\n\t6. Exit")
        ch = int(input("\nEnter your choice: "))
        
        if ch == 1:
            value = int(input("\n\tEnter value to push: "))
            stack_2.push(value)
        elif ch == 2:
            print(stack_2)
        elif ch == 3:
            print(stack_2.pop())
        elif ch == 4:
            stack_1 = Stack()
            print(stack_1)
            stack_1.push(10)
            stack_1.push(20)
            stack_1.push(30)
            print(stack_1)
            print(stack_1.Top())

            print (stack_1.pop())
            stack_1.push(40)
            stack_1.push(50)
            print(stack_1)
            print(stack_1.Top())

            print (stack_1.pop())
            print (stack_1.pop())
            print (stack_1.pop())
            print(stack_1)
            print(stack_1.Top())

            print (stack_1.pop())
            print (stack_1.pop())
            print(stack_1.Top())
            print (stack_1.pop())
        elif ch == 5:
            top = stack_2.top
            maxi = -9999999
            while top is not None:
                if top.data > maxi:
                    maxi = top.data
                top = top.next
            print("Max: ", maxi)
        else:
            break           

    
if __name__ == "__main__":
    main()


'''
OUTPUT:

Stack created
*********************************** Menu ***********************************
	1. Push element into stack 
	2. Display stack 
	3. Pop element from stack 
	4. Default test cases 
	5. Exit

Enter your choice: 1

	Enter value to push: 12
+Pushed:  12
*********************************** Menu ***********************************
	1. Push element into stack 
	2. Display stack 
	3. Pop element from stack 
	4. Default test cases 
	5. Exit

Enter your choice: 1

	Enter value to push: 325
+Pushed:  325
*********************************** Menu ***********************************
	1. Push element into stack 
	2. Display stack 
	3. Pop element from stack 
	4. Default test cases 
	5. Exit

Enter your choice: 1

	Enter value to push: 34
+Pushed:  34
*********************************** Menu ***********************************
	1. Push element into stack 
	2. Display stack 
	3. Pop element from stack 
	4. Default test cases 
	5. Exit

Enter your choice: 2

STACK is:
 -->	| 34 |
	| 325 |
	| 12 |
	------
*********************************** Menu ***********************************
	1. Push element into stack 
	2. Display stack 
	3. Pop element from stack 
	4. Default test cases 
	5. Exit

Enter your choice: 3
-Popped: 34
*********************************** Menu ***********************************
	1. Push element into stack 
	2. Display stack 
	3. Pop element from stack 
	4. Default test cases 
	5. Exit

Enter your choice: 2

STACK is:
 -->	| 325 |
	| 12 |
	------
*********************************** Menu ***********************************
	1. Push element into stack 
	2. Display stack 
	3. Pop element from stack 
	4. Default test cases 
	5. Exit

Enter your choice: 4
Stack created
Stack created...
	Stack is empty!!!
+Pushed:  10
+Pushed:  20
+Pushed:  30

STACK is:
 -->	| 30 |
	| 20 |
	| 10 |
	------
Top is: 30

-Popped: 30
+Pushed:  40
+Pushed:  50

STACK is:
 -->	| 50 |
	| 40 |
	| 20 |
	| 10 |
	------
Top is: 50

-Popped: 50
-Popped: 40
-Popped: 20

STACK is:
 -->	| 10 |
	------
Top is: 10

-Popped: 10
No element to pop!!!
Top is None
No element to pop!!!
*********************************** Menu ***********************************
	1. Push element into stack 
	2. Display stack 
	3. Pop element from stack 
	4. Default test cases 
	5. Exit

Enter your choice: 5
'''