class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

class BST:
    def __init__(self):
        self.root = None

    def insert( self, node, value):

    # If the tree is empty, return a new node
        if node is None:
            return Node(value)

    # Otherwise recur down the tree
        if value < node.value:
            node.left = self.insert(node.left, value)
        else:
            node.right = self.insert(node.right, value)

    # return the (unchanged) node pointer
        return node


    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.value)
            self.inorder(root.right)
    def preorder(self,root):
        if root:
            print(root.value)
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.preorder(root.right)
            print(root.value)

    def minval_node(self,node):
        current = node
        while(current.left is not None):
            current = current.left
        return current

    def deleteNode(self,root,value):
        if root is None:
            return root

        if value<root.value:
            root.left = self.deleteNode(root.left,value)

        elif(value > root.value):
            root.right = self.deleteNode(root.right,value)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.right
                root = None
                return temp
            temp = self.minval_node(root.right)
            root.value = temp.value
            root.right = self.deleteNode(root.right, temp.value)
        print(value," deleted")
        return root


    def search(self,value):
        if self.root!=None:
            return self._search(value,self.root)
        else:
            return False

    def _search(self,value,node):
        if value==node.value:
            return True
        elif value<node.value and node.left != None:
            self._search(value, node.left)
        elif value>node.value and node.right != None:
            self._search(value, node.right)
        return False

print("*"*25, "Delete Node BST", "*"*25)
root = Node(50)
s = BST()
s.insert(root,40)
s.insert(root,30)
s.insert(root,4)
s.insert(root,78)
print("\nInorder :")
s.inorder(root)
print("\nPostorder :")
s.postorder(root)
print("\nPreorder :")
s.preorder(root)
print("\n\tSearch Result :",s.search(50))
print("\n")
s.deleteNode(root,30)
print("\n")
s.preorder(root)
