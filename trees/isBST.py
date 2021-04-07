'''
author: Sharmila S
Date: 06-04-2021

Topic: Check whther the given tree is a BST or not
'''

# local imports
from trees.BinarySearchTree import BinarySearchTree

'''
concept:
    Left child -only has minimum values
    Right child -only has maximum values

algo:
    - pass root, with min(-999), max(999) values
    - function
        - base condition - if node is null - return true
        - check whether node->data is in range (min, max)
        - check root->left is within range(min, root->data)
        - check root->right is within range(root->data, max)
        if all yes - return True
        else - return False
'''

def isBST(root, min, max):

    if (root is None):
        return True
    
    return root.value > min and root.value < max and isBST(root.left, min, root.value) and isBST(root.right, root.value, max)

bst = BinarySearchTree()

nodes = [ 5, 3, 6, 8, 2, 9, 7]
for val in nodes:
    bst.create_node(val)

print(isBST(bst.root, -999, 999))