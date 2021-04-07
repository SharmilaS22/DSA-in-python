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
        res = res + inorderTraversal(root.right)
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

# Postorder traversal
# ab+
def postorderTraversal(root):
    res = []
    if root:
        res = res + postorderTraversal(root.left)
        res = res + postorderTraversal(root.right)
        res.append(root.value)
    return res

print('Inorder traversal', inorderTraversal(bst.root))
print('Preorder traversal', preorderTraversal(bst.root))
print('Postorder traversal', postorderTraversal(bst.root))
