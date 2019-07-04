class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def add_start(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
    
    def add_end(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newNode
            newNode.prev = curr
            
    def add_after_pos(self, pos, data):
        newNode = Node(data)
        curr = self.head
        if curr is None:
            print("inserting data at begining.")
            self.head = newNode
            return
        for i in range(1, pos):
            curr = curr.next
            if curr is None:
                print("Empty list")
                break
        else:
            newNode.next = curr.next
            curr.next.prev = newNode
            curr.next = newNode
            newNode.prev = curr

    def remove(self, key):
        curr = self.head
        if curr is None:
            print("List is already empty!")
        elif curr.data == key:
            self.head = curr.next
            curr.next.prev = None
            print("Removing", key, "...")
            print( key, 'removed successfully ')
        else:
            flag = 0
            while curr.next:
                if curr.data == key:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    curr = None
                    flag = 1
                    break
                curr = curr.next
            else:
                if curr.next is None and curr.data == key:
                    curr.prev.next = None
                    curr = None
                    flag = 1
            print(str(key)+' removed successfully from list!' if flag else str(key)+' not found in list!')        
                
    def search(self, key):
        curr = self.head
        if curr is None:
            print("List is already empty!")
        else:
            while curr:
                if curr.data == key:
                    print("\t", key, "found in list between", curr.prev.data, "and", curr.next.data)
                    break
                curr = curr.next
            else:
                print(key, "not present in the list!")
                
    def reverse(self):
        temp = None
        curr = self.head
        while curr:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            curr = curr.prev
        if temp is not None:
            self.head = temp.prev
            
    def sort(self):
        swapped = 1
        while swapped:
            swapped = 0
            curr = self.head
            while curr.next != None:
                if curr.data > curr.next.data:
                    temp = curr.data
                    curr.data = curr.next.data
                    curr.next.data = temp
                    swapped = 1
                curr = curr.next
        
    def __str__(self):
        curr = self.head
        if curr is None:
            return 'List is empty!'
        else:
            s = 'List is:\n'
            while curr:
                s += str(curr.data) + ' '
                curr = curr.next
            return s                


def main():
    DLL = DoublyLinkedList()                         # creating the Double Linked list
    DLL.add_end(19)                                  # adding element at the end
    DLL.add_end(100)
    DLL.add_start(76)                                # adding element at the start
    DLL.add_end(54)
    DLL.add_after_pos(2, 6)                         # adding element after position
    DLL.add_start(45)
    DLL.add_start(56)
    DLL.add_end(80)
    DLL.add_after_pos(5, 7)
    
    print(DLL)                                       # displaying the list
    
    DLL.remove(54)                                   # deleting element matching the key
    
    print(DLL)
    
    DLL.search(45)                                   # searching the given key element
    
    DLL.sort()                                       # sorting the list
    
    DLL.reverse()                                    # reversing the list
    
    
if __name__ == "__main__":
    main()

