'''
author: Sharmila S
Date: 16-04-2021

Topic: Merge two sorted list
'''

from linkedList.SinglyLinkedList import LinkedList

def mergeLists(head1, head2):
    
    # compare a and b
    # if equall; add both; increment both
    # if a < b; add a; increment a
    # elif b < a; add b; increment b
    
    # add first
    
    if (head1 is None):
        return head2
    if (head2 is None):
        return head1
    
    temp1 = head1
    temp2 = head2
    mergedList = LinkedList()
    
    while (temp1 is not None and temp2 is not None):
        
        if (temp1.data < temp2.data ):
            mergedList.AddNode(temp1.data)
            temp1 = temp1.next
        elif (temp2.data < temp1.data):
            mergedList.AddNode(temp2.data)
            temp2 = temp2.next     
        else:
            mergedList.AddNode(temp1.data)
            mergedList.AddNode(temp2.data)
            temp1 = temp1.next
            temp2 = temp2.next               

    if (temp1 is None and temp2 is not None):
        
        while(temp2 is not None):
            mergedList.AddNode(temp2.data)
            temp2 = temp2.next
    
    elif (temp1 is not None and temp2 is None):
        
        while(temp1 is not None):
            mergedList.AddNode(temp1.data)
            temp1 = temp1.next        
            
    return mergedList


list1 = LinkedList()

list1.AddNode(3)
list1.AddNode(4)
list1.AddNode(6)
list1.AddNode(7)

list1.PrintList()


list2 = LinkedList()

list2.AddNode(1)
list2.AddNode(4)
list2.AddNode(5)
list2.AddNode(9)

list2.PrintList()


merged = mergeLists(list1.head, list2.head)

merged.PrintList()