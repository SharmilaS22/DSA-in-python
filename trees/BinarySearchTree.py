'''
author: Sharmila S
Date: 05-04-2021

Topic: Tree - Binary tree creation
'''

# create a class Node
class Node:

    def __init__(self, value):
        # assign value
        self.value = value
        # initialise left and right child as None
        self.left  = None
        self.right =  None


# binary tree class
class BinarySearchTree:

    def __init__(self) :
        # a tree must have a root
        self.root = None

    def create_node(self, value):

        # check if root exists
        if (self.root == None):
            # if root doesnt exists
            # create a root node
            self.root = Node(value)
        
        else:
            # this part executes when root exists already

            # assign current as root
            current = self.root

            while (True):
            # check whether the root value is lesser or greater than the value
                if (value < current.value):
                    # left child
                    if (current.left): 
                        current = current.left # current.left is our new parent node to search
                    else:
                        current.left = Node(value)
                        break # if current.left is none, assign present value

                elif (value > current.value ):
                    # right child
                    if (current.right): 
                        current = current.right # current.right is our new parent node to search
                    else:
                        current.right = Node(value)
                        break # if current.right is none, assign present value

                else:
                    # no duplicate valules are allowed
                    break


''' create a new tree and print tree '''
# newtree = BinarySearchTree()
# newtree.create_node(5) # first node - root
# newtree.create_node(3) # value lesser than root - left child
# newtree.create_node(6) # value greater than root - right child

# print('Root -> ', newtree.root.value)
# print('Left child -> ', newtree.root.left.value)
# print('Right child -> ', newtree.root.right.value)
