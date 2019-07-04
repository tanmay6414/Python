class Node: 

   
    def __init__(self, data,seatno,present): 
        self.data = data
        self.seatno=seatno
        self.next = None
        self.prev = None
        self.present=present


class DoublyLinkedList: 

    
    def __init__(self): 
        self.head = None
    def append(self, new_data,seatno,present): 
        new_node = Node(new_data,seatno,present)  
        new_node.next = None
        if self.head is None: 
            new_node.prev = None
            self.head = new_node 
            return
        last = self.head 
        while(last.next is not None): 
            last = last.next
        last.next = new_node 
        new_node.prev = last 

        return
    def printList(self, node): 

        print ("\nTraversal in forward direction")
        while(node is not None): 
            print(node.data)
            last = node 
            node = node.next
            
    def push(self, new_data,seatno,present):
        print("push start")
        new_node=Node(new_data,seatno,present)
        new_node.next=self.head
        new_node.prev=None
        if self.head is not None:
            self.head.prev = new_node 
        self.head = new_node
    def deleteNodeend(self,node):
        print ("\nDelete last")
        while(node is not None):
            if node.next==None:
                last.next=None
            last=node
            node = node.next
    def deleteNodeFront(self,node):
        print("\nDelete Front")
        self.head=node.next
        node.next=None
        
llist = DoublyLinkedList() 
seats=int(input("\nEnter number of seats"))
for i in range(1,seats+1):
    llist.append(0,i,'')  
llist.printList(llist.head) 
llist.push(10,10,'new')
llist.push(11,11,'new')
llist.printList(llist.head)
llist.deleteNodeend(llist.head)
llist.printList(llist.head)
llist.deleteNodeFront(llist.head)
llist.printList(llist.head)