class BinaryHeap(object):
    ''' class to create a Binary Heap object using lists'''
    def __init__(self):
        self.items = [(0, 0)]                                       # initializing list with 0 priority so that simple integer division could be used

    def __len__(self):
        ''' overloading the length function to return the correct length of the list'''
        return len(self.items) - 1
    
    def add(self, k):
        ''' method to add a element's information into the list '''
        self.items.append(k)
        self.shift_up()
    
    def shift_up(self):
        ''' method to move the element up to its correct priority position in the list'''
        i = len(self)
        while i // 2 > 0:
            if self.items[i][1] < self.items[i // 2][1]:
                self.items[i // 2], self.items[i] = self.items[i], self.items[i // 2]
            i = i // 2
            
    def shift_down(self, i):
        ''' method to move the element down to its correct priority position in the list'''
        while i * 2 <= len(self):
            mc = self.min_child(i)
            if self.items[i][1] > self.items[mc][1] :
                self.items[i], self.items[mc] = self.items[mc], self.items[i]
            i = mc

    def min_child(self, i):
        ''' method to find the minimum child of the given element'''
        if i * 2 + 1 > len(self):
            return i * 2

        if self.items[i * 2][1] < self.items[i * 2 + 1][1]:
            return i * 2

        return i * 2 + 1
    
    def delete_min(self):
        ''' method to delete the minimum priority element from the list and rearrange the elements properly'''
        if len(self)>1:
            return_value = self.items[1][1]
            self.items[1] = self.items[len(self)]
            self.items.pop()
            self.shift_down(1)
            return return_value
        else:
            return "No elements to remove..."
    
    def build_heap(self, alist):
        ''' method to build the binary heap using the given list directly as an input'''
        i = len(alist) // 2
        self.items = [0] + alist
        while i > 0:
            self.shift_down(i)
            i = i - 1
            
    def display(self):
        ''' method to show the priority list binary heap'''
        print(' '.join(map(str, self.items)))


# In[2]:


def main():
    bh = BinaryHeap()
    
    while True:
        print("*"*25, "Menu", "*"*25)
        print("\n1.Add element's information\n2.Remove a element with highest priority\n3.Display priority queue\n4.Exit")
        ch = int(input("Enter a choice: "))
        if ch == 1:
            print("\tAdd info:")
            element_id = int(input("element_ID: "))
            priority = int(input("Priority: "))
            bh.add((element_id, priority))
        elif ch == 2:
            print("\nRemoving element...")
            print("\t", bh.delete_min(), " removed!")
        elif ch == 3:
            bh.display()
        else:
            break
    
if __name__ == "__main__":
    main()