class Node:
    ''' class to create a node element that stores a word and its meaning to be inserted into BST'''
    def __init__(self, key):
        self.left = None
        self.key = key
        self.right = None
        
class BST:
    ''' class to create a word dictionary using Binary Search Tree using Node class's objects'''
    def __init__(self):
        self.root = None
    
    def insert(self, key, parent=None):
        if parent is None:
            parent = self.root
        if self.root is None:
            self.root = Node(key)
            #print("Added", key, "as root node")
        else:
            if key > parent.key:
                if parent.right is None:
                    #print("\nAdding", key," to ", parent.key, "\'s right")
                    parent.right = Node(key)
                else:
                    parent = parent.right
                    self.insert(key, parent)
            else:
                if parent.left is None:
                    #print("\nAdding", key," to ", parent.key, "\'s left")
                    parent.left = Node(key)
                else:
                    parent = parent.left
                    self.insert(key, parent)

def maxDiffUtil(ptr, k, min_diff, min_diff_key): 
    if ptr == None:  
        return
            
    # If k itself is present  
    if ptr.key == k: 
        min_diff_key[0] = k  
        return

    # update min_diff and min_diff_key by   
    # checking current node value  
    if min_diff > abs(ptr.key - k): 
        min_diff = abs(ptr.key - k)  
        min_diff_key[0] = ptr.key 

    # if k is less than ptr->key then move  
    # in left subtree else in right subtree  
    if k < ptr.key: 
        maxDiffUtil(ptr.left, k, min_diff,  
                                    min_diff_key) 
    else: 
        maxDiffUtil(ptr.right, k, min_diff,  
                                    min_diff_key) 
  
# Wrapper over maxDiffUtil()  
def maxDiff(root, k): 
      
    # Initialize minimum difference  
    min_diff, min_diff_key = 999999999999, [-1] 
  
    # Find value of min_diff_key (Closest  
    # key in tree with k)  
    maxDiffUtil(root, k, min_diff, min_diff_key) 
  
    return min_diff_key[0] 
                    

'''
                    38
            23              56      
        2       30       52    64
           12                     98   
          6                     74
'''

bst = BST()
bst.insert(38)
bst.insert(23)
bst.insert(2)
bst.insert(30)
bst.insert(56)
bst.insert(64)
bst.insert(12)
bst.insert(52)
bst.insert(6)
bst.insert(98)
bst.insert(74)

num = int(input("Find closest to: "))
print(maxDiff(bst.root, num)) 

