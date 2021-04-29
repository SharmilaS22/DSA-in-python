'''
author: Sharmila S
Date: 16-04-2021

Topic: Middle element
'''
# local imports
import sys
sys.path.append(r"D:\sharmi-projects\DSA_py")

from linkedList.SinglyLinkedList import LinkedList, Node

def middleElement(head):

    half = head
    last = head

    while last and last.next:
        half = half.next
        last = last.next.next

    return half.data

list1 = LinkedList()
list1.AddNode(2)
list1.AddNode(3)
list1.AddNode(5)
list1.AddNode(6)
list1.AddNode(7)

print(middleElement(list1.head))

