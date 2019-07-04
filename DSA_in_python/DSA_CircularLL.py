#Represents the node of list.    
class Node:    
  def __init__(self,data):    
      self.data = data
      self.next = None

  def get_data(self):
      return self.data
    
  def get_next(self):
      return self.next
    
  def set_next(self, node):
      self.next = node      
     
class CreateList:    
  #Declaring head and tail pointer as null.    
  def __init__(self):    
    self.head = Node(None)    
    self.tail = Node(None)    
    self.head.next = self.tail    
    self.tail.next = self.head    
        
  #This function will add the new node at the end of the list.    
  def add_at_end(self,data):    
    newNode = Node(data)    
    #Checks if the list is empty.    
    if self.head.data is None:    
      #If list is empty, both head and tail would point to new node.    
      self.head = newNode    
      self.tail = newNode    
      newNode.next = self.head    
    else:    
      #tail will point to new node.    
      self.tail.next = newNode    
      #New node will become new tail.    
      self.tail = newNode    
      #Since, it is circular linked list tail will point to head.    
      self.tail.next = self.head    

  def add_atbeginning(self,data):
    newNode = Node(data)
    current = self.head
    newNode.next = self.head

    if not self.head:
      newNode.next = newNode
    else:
      while current.next != self.head:
        current = current.next
      current.next = newNode
    self.head = newNode

  def add_mid(self,pos,data):
    newNode = Node(data)
    current = self.tail.next

    for i in range(pos):
      current = current.next
      if current == self.tail:
        print("Position out of Linits")
        break
    
    newNode.next = current.next
    current.next = newNode
    if current == self.tail:
      self.tail = newNode

  
  

  def remove(self,key):
    if self.head.data == key:
      current = self.head
      while current.next != self.head:
        current = current.next
      current.next = self.head.next
      self.head = self.head.next
    else:
      current = self.head
      tail = None
      while current.next != self.head:
        tail = current
        current = current.next
        if current.data == key:
          tail.next = current.next
          current = current.next


  def search(self, index):
    current = self.head
    count = 0
    while(current):
      if (count==index):
        return current.data
      count+=1
      current = current.next

    assert(False)
    return 0  

#Displays all the nodes in the list    
  def display(self):    
    current = self.head    
    if self.head is None:    
      print("List is empty")    
      return    
    else:    
        print("\tNodes of the circular linked list: \n")    
        #Prints each node by incrementing pointer.    
        print(current.data)    
        while(current.next != self.head):    
            current = current.next    
            print(current.data)

  def sort_CL(self):
    ''' method to sort the linked list in ascending order'''
    #last = None
    swapped = 1
    while swapped:
      current = self.tail.next
      swapped = 0
      while current.get_next() != self.tail:
        if current.get_data() > current.get_next().get_data():
          temp = current.get_data()
          current.data = current.get_next().get_data()
          current.get_next().data = temp
          swapped = 1
        current = current.get_next()
      #last = current
    print("\n\t Sorted Linked list is:\n")
    self.display()

  def reverse_CL(self):
        ''' method to reverse the linked list'''
        current = self.head
        prev = None
        while current:
            next = current.get_next()
            current.set_next(prev)
            prev = current
            current = next
        self.head = prev
        print("\n\tReversed Linked list is: \n")
        self.display()
  

  
     
cl = CreateList()    
#Adds data to the list    
cl.add_at_end("Hamburgers")    
cl.add_at_end("Mac_burger")    
cl.add_atbeginning("Cheese_burgers")    
cl.add_atbeginning("Grilled_burgers")   
cl.add_mid(1,"DoubleCheese_burgers")
  #Displays all the nodes present in the list    
cl.display()
print("\n")
cl.remove("s")
cl.display()
print("\n")
print("Element at index 2 is: ",cl.search(2))
print("\n")
cl.sort_CL()
print("\n")
cl.reverse_CL()
