'''
author: Sharmila S
Date: 16-04-2021

Topic: Remove duplicates
'''

# local imports
import sys
sys.path.append(r"D:\sharmi-projects\DSA_py")

from linkedList.SinglyLinkedList import LinkedList

def removeDuplicates(head):
    
    duplicate = []
    temp = head
    prev = None
    
    if (head is None):
        return
    
    while (temp.next is not None):
        info = temp.data
        print(info)
        
        if (info in duplicate):
            prev.next = temp.next

        else:
            duplicate.append(info)
            prev = temp
        
        temp = temp.next
        
    if (temp.data in duplicate):
        prev.next = temp.next
        
    # print(duplicate)
    return head

list1 = LinkedList()
list1.AddNode(2)
list1.AddNode(3)
list1.AddNode(2)
list1.AddNode(5)
list1.AddNode(6)
list1.AddNode(6)

list1.PrintList()

# call removeDuplicates()
removeDuplicates(list1.head)

list1.PrintList()