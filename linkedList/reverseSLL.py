'''
author: Sharmila S
Date: 15-04-2021

Topic: reverse a linked list
'''

# local imports
import sys
sys.path.append(r"D:\sharmi-projects\DSA_py")

from linkedList.SinglyLinkedList import LinkedList

def ReverseLL(head):

    current = head
    prev = None

    while (current is not None):

        next = current.next

        current.next = prev

        prev = current
        current = next

    head = prev
    return head



newlist = LinkedList()
newlist.AddNode(2)
newlist.AddNode(3)
newlist.AddNode(4)
newlist.AddNode(5)
newlist.AddNode(6)

newlist.PrintList()

newlist.head = ReverseLL(newlist.head)

newlist.PrintList()
