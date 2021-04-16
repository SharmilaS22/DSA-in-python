'''
author: Sharmila S
Date: 14-04-2021

Topic: Doubly Linkedlist 
'''

class Node():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class DLList():

    def __init__(self) -> None:
        self.head = None

    def InsertNode(self, data):

        # create a new node
        newnode = Node(data)

        # algorithm--
        # check whther head is none
            # first node - head = node

        # head is not none
            # traverse to last node, with prev
            # set prev->right = newnode, 
            # set newnode->left = prev

        if (self.head is None):
            self.head = newnode
            return
        
        temp = self.head
        while (temp.right is not None):
            temp = temp.right

        temp.right   = newnode
        newnode.left = temp

    def DeleteNode(self, _data):
        
        # algorithm
        # check each node whther it has the data
        
        # prev, temp(current)
        # if the node to be deleted is first node
            # make head point to second elem, and second elem's left is None
        # else prev.right = temp.right, temp.right node's left point back to prev
        # del temp

        temp = self.head
        prev = None
        while( temp.right is not None):
            if (temp.data == _data):
                if(prev is not None):
                    prev.right = temp.right
                    temp.right.left = prev
                else:
                    self.head = temp.right
                    temp.right.left = None
                del temp
                break
            prev = temp
            temp = temp.right

    def PrintList(self):

        # algrithm
        # if head is none - no elements
            # print('no elements')
            # return
        
        # head is not none - some elements are present
        # temp = head (start from head)
        # while temp is not the last one
            # print data 
            # increment temp to next node
        
        if (self.head is None):
            return
        
        temp = self.head
        while(temp.right is not None):
            print(temp.data, ' -> ', end='')
            temp = temp.right
        print(temp.data)

    def PrintBothDirection(self):

        temp = self.head

        print('None <-', temp.data, '-> ', temp.right.data)
        temp = temp.right

        while(temp.right is not None):
            print( temp.left.data,'<-', temp.data, '->', temp.right.data )
            temp = temp.right

        print(temp.left.data, '<-', temp.data, '-> None')

# list2 = DLList()

# list2.InsertNode(3)
# list2.InsertNode(4)
# list2.InsertNode(5)
# list2.InsertNode(6)

# list2.PrintList()

# list2.DeleteNode(3)
# list2.PrintList()

# list2.DeleteNode(5)
# list2.PrintList()

# list2.PrintBothDirection()
