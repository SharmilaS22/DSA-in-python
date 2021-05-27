'''
author: Sharmila S
Date: 27-05-2021

Topic: Level Order Traversal
'''

# local imports
import sys
sys.path.append(r"D:\sharmi-projects\DSA_py")

from trees.BinarySearchTree import BinarySearchTree

bst = BinarySearchTree()

nodes = [ 5, 3, 6, 8, 2, 9, 7]
for val in nodes:
    bst.create_node(val)


def levelOrderTraversal(root):

    if (root is None):
        return

    # add root to queue
    queue = []
    queue.append(root)

    while (len(queue) > 0):

        # dequeue first elem
        print(queue[0].value, end=" ")
        temp = queue.pop(0)

        if (temp.left is not None):
            queue.append(temp.left)
        if (temp.right is not None):
            queue.append(temp.right)
            

levelOrderTraversal(bst.root)