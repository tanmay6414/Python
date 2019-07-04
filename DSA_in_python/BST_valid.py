from sys import maxsize
from random import randint

class Node(object):
    def __init__(self, key):
        self.key   = key
        self.left  = None
        self.right = None
    
class BST(object):
    def __init__(self):
        self.root = None
    
    def insert(self, key, parent=None):
        '''method to insert a new word into the dictionary BST'''
        if parent is None:
            parent = self.root
        if self.root is None:
            self.root = Node(key)
            print("Added", key, "as root node")
        else:
            if key > parent.key:                                            # Traverse the right sub-tree if key > current node
                if parent.right is None:
                    print("\nAdding", key,"to", parent.key, "\'s right")
                    parent.right = Node(key)
                else:
                    parent = parent.right
                    self.insert(key, parent)
            else:                                                           # Traverse the left sub-tree if key < current node
                if parent.left is None:         
                    print("\nAdding", key,"to", parent.key, "\'s left")
                    parent.left = Node(key)
                else:
                    parent = parent.left
                    self.insert(key, parent)

    def isBST(self):
        return self.isBSTvalid(self.root, -maxsize, maxsize)

    def isBSTvalid(self, node, mini, maxi):
        if node is None:
            return True
        if node.key < mini or node.key > maxi:
            print("Breaker: ", node.key, mini, maxi)
            return False
        
        return self.isBSTvalid(node.left, mini, node.key-1) and self.isBSTvalid(node.right, node.key+1, maxi)


def main():
    bst = BST()
    height = 3
    n = 2**height - 1
    for _ in range(n):
        bst.insert(randint(1, 100))
    print(bst.isBST())

    bst1 = BST()
    bst1.root = Node(3)
    bst1.root.left = Node(2)
    bst1.root.right = Node(5)  
    bst1.root.right.left = Node(1)  
    bst1.root.right.right = Node(4) 
    print(bst.isBST())
    

if __name__ == "__main__":
    main()