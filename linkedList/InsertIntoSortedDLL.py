'''
author: Sharmila S
Date: 16-04-2021

Topic: Insert into Sorted DLL
'''

from linkedList.DoubleLinkedList import DLList, Node

def sortedInsert(head, _data):
    
    # while < data move
    # insert node
    
    temp = head
    prev = None
    newnode = Node(_data)
    
    while (temp is not None):
        if (temp.data > _data):
            # add between prev and temp
            
            # prev.right -> newnode
            # newnode.left -> prev
            # newnode.right -> temp
            # temp.left -> newnode
            if (prev is None): #add at start
                head = newnode
                newnode.left = None

            else:              # add at tail
                prev.right    = newnode
                newnode.left = prev

            newnode.right = temp
            temp.left    = newnode

            return head
            
        prev = temp
        temp = temp.right
        
    # if all element is lesser
    # add at end
    prev.right    = newnode
    newnode.left = prev
    
    return head


list1 = DLList()

list1.InsertNode(3)
list1.InsertNode(4)
list1.InsertNode(6)
list1.InsertNode(7)

list1.PrintList()

list1.head = sortedInsert(list1.head, 1)
list1.head = sortedInsert(list1.head, 5)
list1.head = sortedInsert(list1.head, 9)

list1.PrintList()
print("------------")
list1.PrintBothDirection()


