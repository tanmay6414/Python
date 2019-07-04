import sys
import random
random.seed(0)

class Node:
    def __init__(self, key):
        self.left = None
        self.key = key
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        print("Creating Binary search tree...\n")
    
    def insert(self, key, parent=None):
        if parent is None:
            parent = self.root
        if self.root is None:
            self.root = Node(key)
            #print("Added", key, "as root node")
        else:
            if key > parent.key:                                            # Traverse the right sub-tree if key > current node
                if parent.right is None:
                    #print("\nAdding", key,"to", parent.key, "\'s right")
                    parent.right = Node(key)
                else:
                    parent = parent.right
                    self.insert(key, parent)
            else:                                                           # Traverse the left sub-tree if key < current node
                if parent.left is None:         
                    #print("\nAdding", key,"to", parent.key, "\'s left")
                    parent.left = Node(key)
                else:
                    parent = parent.left
                    self.insert(key, parent)   
                       
    def inorder(self, node=1):
        '''method to print BST inorder (left, root, right)'''
        if node == 1:
            node = self.root
            print("\nBST is: (inorder)\n")
        if node:
            self.inorder(node.left)
            print("\t", node.key, end=", ")
            self.inorder(node.right)
  
    def kth_smallest(self, k, arr=[], node=1):
        '''method to print BST inorder (left, root, right)'''
        if node == 1:
            node = self.root
        if node:
            self.kth_smallest(k, arr, node.left)
            arr.append(node.key)
            if len(arr) == k:
                print("\n\tk-th smallest is: ", arr[-1])
                sys.exit()
            self.kth_smallest(k, arr, node.right)

def main():
    bst = BST()
    height = 3
    n = 2**height - 1
    for _ in range(n):
        bst.insert(random.randint(1, 100))
    bst.inorder()
    k = int(input("\nk=?: "))
    bst.kth_smallest(k)


if __name__ =="__main__":
    main()
