# DFS traversal of a tree using recursion
# DFS (Depth-first search) is technique used for traversing tree or graph. 
# Here backtracking is used for traversal. In this traversal first the deepest node is visited and then backtracks to it’s parent node if no sibling of that node exist. 

class Node:
    def __init__(self, key):
        self.left = None
        self.value = key
        self.right = None

class Traversal:
    def inOrder(self, root):
        if root :
            self.inOrder(root.left)
            print(root.value)
            self.inOrder(root.right)

    def preOrder(self, root):
        if root :
            print(root.value)
            self.preOrder(root.left)
            self.preOrder(root.right)

    def postOrder(self, root):
        if root :
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.value)


# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

traveral = Traversal()

print ("InOrder traversal of binary tree is")
traveral.inOrder(root)

print ("PreOrder traversal of binary tree is")
traveral.preOrder(root)

print ("PostOrder traversal of binary tree is")
traveral.postOrder(root)