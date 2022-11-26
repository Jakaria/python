##########################################################################
# Recursive directory traversal and print all the file names
# Recursive function with the help of OS module

import os

class Node:
    def __init__(self, dir):
        self.left = None
        self.path = dir
        self.right = None

class Traversal:
    def inOrder(self, root):
        if os.path.isdir(root.path):
            # print all the file names in current directory
            for currentPath, subDirectories, files in os.walk(root.path):
                for file in files:
                    print(os.path.join(currentPath, file))
            # find all the sub directories and recursively traversing
            for subDirPath in os.listdir(root.path):
                self.inOrder(Node(subDirPath))       

# Driver code
root = Node(".")
traveral = Traversal()
traveral.inOrder(root)


# Python 3 Built In Method
# import glob, os
# for filename in glob.iglob('./**', recursive=True):
#     if os.path.isfile(filename): # filter dirs
#         print(filename)
##########################################################################