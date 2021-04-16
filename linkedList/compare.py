'''
author: Sharmila S
Date: 15-04-2021

Topic: Compare two linked list
'''

from linkedList.SinglyLinkedList import LinkedList

def compare_lists(head1, head2):
    
    temp1 = head1
    temp2 = head2
    
    while( temp1 is not None and temp2 is not None):
        
        if ( temp1.data != temp2.data ):
            return 0
        
        temp1 = temp1.next
        temp2 = temp2.next
        
    if (temp1 is None and temp2 is None ):
        return 1
    return 0

list1 = LinkedList()
list1.AddNode(2)
list1.AddNode(3)
list1.AddNode(4)
list1.AddNode(5)
list1.AddNode(6)

list2 = LinkedList()
list2.AddNode(2)
list2.AddNode(3)
list2.AddNode(9)
list2.AddNode(5)
list2.AddNode(6)

print( compare_lists(list1.head, list2.head) )