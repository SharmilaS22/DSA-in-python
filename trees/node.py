'''
author: Sharmila S
Date: 05-04-2021

Topic: Tree - Node creation
'''

# create a class Node

class Node:

    def __init__(self, value):
        # assign value
        self.value = value
        # initialise left and right child as None
        self.left  = None
        self.right =  None

# create a node
root = Node(5)

print('value -> ', root.value)
print('left -> ', root.left)
print('right -> ', root.right)