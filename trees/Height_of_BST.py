from trees.BinarySearchTree import BinarySearchTree

def height(root):
    
    if ( root is None ):
        return -1
    
    leftheight = 0
    rightheight = 0
    
    if (root.left is not None ):
        leftheight = 1 + height(root.left)
    if ( root.right is not None):
        rightheight = 1 + height(root.right)
        
    return max(leftheight, rightheight)

bst = BinarySearchTree()

nodes = [ 5, 3, 6, 8, 2, 9, 7]
for val in nodes:
    bst.create_node(val)

print('Height of the tree: ', height(bst.root))