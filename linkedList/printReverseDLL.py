'''
author: Sharmila S
Date: 16-04-2021

Topic: reverse print DLL
'''

from linkedList.DoubleLinkedList import DLList


def reversePrint(head):
    
    if (head is None):
        return
    
    prev = None
    curr = head
    
    while (curr is not None):
        
        # swapping prev
        temp       = curr.left
        curr.left  = curr.right
        curr.right = temp

        prev = curr        
        curr = curr.left
        
    # last one - point to head
    # head = prev
    return prev


list2 = DLList()

list2.InsertNode(3)
list2.InsertNode(4)
list2.InsertNode(5)
list2.InsertNode(6)

list2.PrintList()
list2.PrintBothDirection()

list2.head = reversePrint(list2.head)

list2.PrintList()
list2.PrintBothDirection()