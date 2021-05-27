'''
author: Sharmila S
Date: 07-04-2021

Topic: Inorder traversal
'''

# local imports
from trees.BinarySearchTree import BinarySearchTree

bst = BinarySearchTree()

nodes = [ 5, 3, 6, 8, 2, 9, 7]
for val in nodes:
    bst.create_node(val)
    
'''
    +
 a     b

 inorder ->    a+b
 preorder ->   +ab
 postorder ->  ab+

'''

# Inorder traversal
# a+b
def inorderTraversal(root):
    res = []
    if root:
        res = inorderTraversal(root.left)
        res.append(root.value)
        res.extend( inorderTraversal(root.right) )
    return res

# Preorder traversal
# +ab
def preorderTraversal(root):
    res = []
    if root:
        res.append(root.value)
        res = res + preorderTraversal(root.left)
        res = res + preorderTraversal(root.right)
    return res

#  we can retrieve all the data in sorted order using in-order traversal.


# Postorder traversal
# ab+
def postorderTraversal(root):
    res = []
    if root:
        res = res + postorderTraversal(root.left)
        res = res + postorderTraversal(root.right)
        res.append(root.value)
    return res

# It is worth noting that when you delete nodes in a tree,
#  deletion process will be in post-order.
#  That is to say, when you delete a node, you will delete its left child 
# and its right child before you delete the node itself.
# Also, post-order is widely use in mathematical expression.
#  It is easier to write a program to parse a post-order expression. 


print('Inorder traversal', inorderTraversal(bst.root))
print('Preorder traversal', preorderTraversal(bst.root))
print('Postorder traversal', postorderTraversal(bst.root))
