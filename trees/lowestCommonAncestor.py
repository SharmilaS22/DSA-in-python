'''
author: Sharmila S
Date: 06-04-2021

Topic: Find Common Ancestor for two nodes
'''

# local imports
from trees.BinarySearchTree import BinarySearchTree


# if both value is on the left/right side
#   check the left/right side again
# else (both value is in different subtree)
#   return the current node (common ancestor)

def lca(root, val1, val2):

    if (val1 > root.value and val2 > root.value):
        # greater - right child
        return lca(root.right, val1, val2)
    elif (val1 < root.value and val2 < root.value):
        # lesser - left child
        return lca(root.left, val1, val2)
    else:
        # common node 
        return root

bst = BinarySearchTree()

nodes = [ 5, 3, 6, 8, 2, 9, 7]
for val in nodes:
    bst.create_node(val)

print(lca(bst.root, 2, 9).value)
