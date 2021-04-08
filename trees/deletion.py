'''
author: Sharmila S
Date: 08-04-2021

Topic: Deletion of a node
'''

# local imports
from trees.BinarySearchTree import BinarySearchTree
from trees.traversal import inorderTraversal

# https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/

def minValueNode(node):
    current = node
 
    # loop down to find the leftmost leaf
    while(current.left is not None):
        current = current.left
 
    return current


def deleteNode(root, val):
 
    # Base Case
    if root is None:
        return root
 
    # If the value to be deleted
    # is smaller than the root's
    # value then it lies in  left subtree
    if val < root.value:
        root.left = deleteNode(root.left, val)
 
    # If the kye to be delete
    # is greater than the root's value
    # then it lies in right subtree
    elif(val > root.value):
        root.right = deleteNode(root.right, val)

    # If value is same as root's value, then this is the node
    # to be deletedvalue
    else:
 
        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
 
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Node with two children:
        # Get the inorder successor
        # (smallest in the right subtree)
        # (largest in the left subtree)
        temp = minValueNode(root.right)
 
        # Copy the inorder successor's
        # content to this node
        root.value = temp.value
 
        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.value)
 
    return root


# bst
bst = BinarySearchTree()

nodes = [ 5, 3, 6, 8, 2, 9, 7]
for val in nodes:
    bst.create_node(val)



print(inorderTraversal(bst.root))

print(deleteNode(bst.root, 5))

print(inorderTraversal(bst.root))