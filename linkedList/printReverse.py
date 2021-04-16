'''
author: Sharmila S
Date: 15-04-2021

Topic: print in reverse order
'''

from linkedList.SinglyLinkedList import LinkedList

def reversePrint(head):
    # algorithm
    # recursive method

    if head is None:
        # last elem
        return 
    
    reversePrint(head.next) #
    print(head.data)

newlist1 = LinkedList()
newlist1.AddNode(2)
newlist1.AddNode(3)
newlist1.AddNode(4)
newlist1.AddNode(5)
newlist1.AddNode(7)

newlist1.PrintList()

reversePrint(newlist1.head)



