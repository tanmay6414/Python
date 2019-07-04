class Node:
    '''class to define basic methods for Singly Linked List'''
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_next(self, node):
        self.next = node


    ''' Class to create a Singly Linked List '''
    def __init__(self):
        self.head = None

    def add_Start(self, newdata):

        ''' method to add node at the start of the linked list'''
        newNode = Node(newdata)
        newNode.set_next(self.head)
        self.head = newNode
    
    def add_Mid(self, key, newdata):
        ''' method to add node in between two nodes of the linked list'''
        newNode = Node(newdata)
        curr = self.head
        while curr.get_next():
            if curr.get_data() == key:
                break
            curr = curr.get_next()
        newNode.set_next(curr.get_next())
        curr.set_next(newNode)

    def add_End(self, newdata):
        ''' method to add node at the end of the linked list'''
        newNode = Node(newdata)
        if self.head is None:
            self.head = newNode
        else:
            curr = self.head
            while curr.get_next():
                curr = curr.get_next()
            curr.set_next(newNode)
   

    def remove_Start(self):
        ''' method to remove node from the begining of the linked list'''
        print("\n")
        curr = self.head
        self.head = curr.get_next()
        curr = None
        print("\n\t  first element removed successfully!")
        
    def remove(self, key):
        ''' method to remove node in between two nodes of the linked list'''
        print("\n ", key, "is getting removed")
        curr = self.head
        if curr is None:
            print("Linked List is empty!")
            return
        elif curr.get_data() == key:
            self.head = curr.get_next()
            curr = None
        else:
            while curr:
                if curr.get_data() == key:
                    break	
                prev = curr
                curr = curr.get_next()
            prev.set_next(curr.get_next())
            curr = None
        print("\n\t\'", key, "\' removed successfully!")
            
    def remove_End(self):
        ''' method to remove node from the last of the linked list'''
        curr = self.head
        if curr is None:
            print ("\tLinked list is empty!!!")
            return
        while curr:
            if curr.get_next() is None:
                break
            prev = curr
            curr = curr.get_next()
        prev.next = None
        curr = None
        print("\n\t Removed last element successfully!")
        
    def search(self, key):
        ''' method to search a given node in the linked list'''
        curr = self.head
        if curr is None:
            print ("\tLinked list is empty!!!")
        else:
            print("\nSearching", key)
            prev = None
            while curr.get_next():
                if curr.get_data() == key:
                    print("\n\tFound after: \'", prev.get_data(), "\' and before: \'", curr.get_next().get_data(), "\'")
                    break
                prev = curr
                curr = curr.get_next()
            else:
                print("\n\tSoory! It's not available")

    def print_LL(self):
        ''' method print the linked list'''
        curr = self.head
        if curr is None:
            print ("\tLinked list is empty!")
        else:
            while curr:
                print (curr.get_data())
                curr = curr.get_next()
                
    def reverse_LL(self):
        ''' method to reverse the linked list'''
        curr = self.head
        prev = None
        while curr:
            next = curr.get_next()
            curr.set_next(prev)
            prev = curr
            curr = next
        self.head = prev
        print("\n\tReversed Linked list is: \n")
        self.print_LL()
                
    def sort_LL(self):
        ''' method to sort the linked list in ascending order'''
        last = None
        swapped = 1
        while swapped:
            curr = self.head
            swapped = 0
            while curr.get_next() != last:
                if curr.get_data() > curr.get_next().get_data():
                    temp = curr.get_data()
                    curr.data = curr.get_next().get_data()
                    curr.get_next().data = temp
                    swapped = 1
                curr = curr.get_next()
            last = curr
        print("\n\t Sorted Linked list is:\n")
        self.print_LL()




def main():
    SLL = SLinkedList()                          # Create a  Singly linked list
    
    SLL.add_End("Bacon Burger")                # Insert at end 
    SLL.add_Start("Umami Burgers")                      # Insert at begining
    SLL.add_Start("Softdrinks")
    SLL.add_End("Frenchfries")

    SLL.add_End("Pug Burgers")
    
    SLL.add_Mid("Green Chille", "Minetta")            # Insert after key
    SLL.add_Mid("Cheddar", "Onion-Smashed")

    SLL.add_Start("Beef")

    SLL.add_Mid("Hamburgers", "Salmon")

    SLL.add_End("Chile-stuffed")
    
    SLL.add_End("Turkey")

    print("\n\tYour order is: \n")
    SLL.print_LL()                                # Print linked list
    
    SLL.remove("Bacon Burger")

    SLL.remove("Softdrinks")
    
    SLL.search("Frenchfries")
    SLL.search("Crunchy Roll")
    
    SLL.sort_LL()
    
    SLL.reverse_LL()
    
    
if __name__ == "__main__":
    main()


''' OUTPUT:
	Your order is: 

Beef
Softdrinks
Umami Burgers
Bacon Burger
Frenchfries
Pug Burgers
Minetta
Onion-Smashed
Salmon
Chile-stuffed
Turkey
('\n ', 'Bacon Burger', 'is getting removed')
("\n\t'", 'Bacon Burger', "' removed successfully!")
('\n ', 'Softdrinks', 'is getting removed')
("\n\t'", 'Softdrinks', "' removed successfully!")
('\nSearchi', 'Frenchfries')
("\n\tFound after: '", 'Umami Burgers', "' and before: '", 'Pug Burgers', "'")
('\nSearchi', 'Crunchy Roll')

	Soory! It's not available

	 Sorted Linked list is:

Beef
Chile-stuffed
Frenchfries
Minetta
Onion-Smashed
Pug Burgers
Salmon
Turkey
Umami Burgers

	Reversed Linked list is: 

Umami Burgers
Turkey
Salmon
Pug Burgers
Onion-Smashed
Minetta
Frenchfries
Chile-stuffed
Beef '''
