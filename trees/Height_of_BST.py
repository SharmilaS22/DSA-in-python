'''
author: Sharmila S
Date: 05-04-2021

Topic: BST - height of a tree
'''
# local imports
from trees.BinarySearchTree import BinarySearchTree

# height function
def height(root):
    
    if ( root is None ):
        return -1
    
    # initialise leftcount and rightcount
    leftheight = 0
    rightheight = 0
    
    if (root.left is not None ):
        # call recursively to find height of left
        leftheight = 1 + height(root.left)
    if ( root.right is not None):
        # call recursively to find height of right
        rightheight = 1 + height(root.right)
        
    # return the max height
    return max(leftheight, rightheight)

bst = BinarySearchTree()

nodes = [ 5, 3, 6, 8, 2, 9, 7]
for val in nodes:
    bst.create_node(val)

print('Height of the tree: ', height(bst.root))