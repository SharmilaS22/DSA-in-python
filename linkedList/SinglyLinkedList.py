'''
author: Sharmila S
Date: 13-04-2021

Topic: Linkedlist creation, insertion, deletion, printing.
'''

class Node:
    def __init__(self, data) -> None:
        self.data = data;
        self.next = None;
    
class LinkedList:

    def __init__(self):
        self.head = None;

    def AddNode(self, data):
        newnode = Node(data)

        if( self.head is None ):
            self.head = newnode
            return
        
        temp = self.head
        while (temp.next is not None):
            temp = temp.next
        
        temp.next = newnode
        return

    def DeleteNode(self, _data):

        temp = self.head
        prev = None

        while(temp.next is not None):
            
            if(temp.data == _data):
                if(prev is None):
                    self.head = temp.next
                else:
                    prev.next = temp.next
                return
            else:
                prev = temp
                temp = temp.next
            


    def PrintList(self):

        if(self.head is None):
            return

        temp = self.head
        while(temp.next is not None):
            print(temp.data, ' -> ', end='')
            temp = temp.next

        print(temp.data)
        return



# print('hello')
# list1 = LinkedList()
# list1.AddNode(2)
# list1.AddNode(3)
# list1.AddNode(4)
# list1.AddNode(6)
# list1.PrintList()
# list1.DeleteNode(2)
# list1.PrintList()
# list1.DeleteNode(4)
# list1.PrintList()