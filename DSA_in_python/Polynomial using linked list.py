
# coding: utf-8

# In[1]:


class Node:
    ''' class to create a node element for the Linked list polynomial'''
    def __init__(self, coeff, exp):
        self.coeff = coeff
        self.exp = exp
        self.next = None


# In[2]:


class SLinkedList:
    ''' class to create a polynomial using linked list through class Node's object as terms of the polynomial'''
    def __init__(self):
        self.head = None

    def add_Start(self, coeff, exp):
        ''' method to add a polynomial term at the start'''
        newNode = Node(coeff, exp)
        newNode.next = self.head
        self.head = newNode

    def add_End(self, coeff, exp):
        ''' method to add a polynomial term at the end'''
        newNode = Node(coeff, exp)
        if self.head is None:
            self.head = newNode
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newNode
            
    def sort_LL(self):
        ''' method to sort the Linked list / polynomial'''
        print("Sorted linked list:")
        last = None
        swapped = 1
        while swapped:
            curr = self.head
            swapped = 0
            while curr.next != last:
                if curr.exp > curr.next.exp:
                    temp_exp = curr.exp
                    temp_coeff = curr.coeff
                    curr.exp = curr.next.exp
                    curr.coeff = curr.next.coeff
                    curr.next.exp = temp_exp
                    curr.next.coeff = temp_coeff
                    swapped = 1
                curr = curr.next
            last = curr
    
    def __str__(self):
        ''' Overloading the print method to print the polynomial'''
        s = ''
        curr = self.head
        if curr is None:
            print ("\tLinked list is empty!!!")
        else:
            while curr.next:
                s += "(" + str(curr.coeff) + "x^" + str(curr.exp) + ")" + " + "
                curr = curr.next
            s += "(" + str(curr.coeff) + "x^" + str(curr.exp) + ")"
        return s
            
    def __add__(self, other):
        ''' Overloading the '+' operator to perform addition of two polynomials using lined list '''
        result = SLinkedList()  
        f_ptr = self.head                                                        # pointer to head of first polynomial
        s_ptr = other.head                                                       # pointer to head of second polynomial
        
        while True:                                                    
            if f_ptr.exp > s_ptr.exp:
                result.add_End(f_ptr.coeff, f_ptr.exp)
                f_ptr = f_ptr.next
            elif s_ptr.exp > f_ptr.exp:
                result.add_End(s_ptr.coeff, s_ptr.exp)
                s_ptr = s_ptr.next
            else:
                result.add_End(f_ptr.coeff + s_ptr.coeff, f_ptr.exp)
                f_ptr = f_ptr.next
                s_ptr = s_ptr.next
                
            if f_ptr is None:                                                     # Add remaining terms of 2nd polynomial if 1st polynomial has fewer terms
                while s_ptr:
                    result.add_End(s_ptr.coeff, s_ptr.exp)
                    s_ptr = s_ptr.next
                break
            elif s_ptr is None:                                                   # Add remaining terms of 1st polynomial if 2nd polynomial has fewer terms
                while f_ptr:
                    result.add_End(f_ptr.coeff, f_ptr.exp)
                    f_ptr = f_ptr.next
                break
        return result


# In[3]:


def main():
    poly_1 = SLinkedList()
    poly_1.add_End(7, 4)
    poly_1.add_End(12, 3)
    poly_1.add_End(2, 2)
    poly_1.add_End(4, 1)
    
    poly_2 = SLinkedList()
    poly_2.add_End(5, 4)
    poly_2.add_End(8, 2)
    poly_2.add_End(3, 1)
    poly_2.add_End(2, 0)
    
    print("\t  ", poly_1)
    print("+")
    print("\t  ", poly_2)
    
    print("-"*50)
    
    poly_3 = poly_1 + poly_2
    print ("= ", poly_3)
    
if __name__ == "__main__":
    main()


'''
    OUTPUT:

	   (7x^4) + (12x^3) + (2x^2) + (4x^1)
+
	   (5x^4) + (8x^2) + (3x^1) + (2x^0)
--------------------------------------------------
=  (12x^4) + (12x^3) + (10x^2) + (7x^1) + (2x^0)
'''

