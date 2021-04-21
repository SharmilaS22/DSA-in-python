# https://medium.com/techie-delight/queue-data-structure-practice-problems-and-interview-questions-f459bf0578db

'''
author: Sharmila S
Date: 21-04-2021

Topic: Queue using linked list
'''

class Node:
    def __init__(self, _data):
        self.data = _data
        self.next = None

class Queue:

    def __init__(self):
        self.front = None
        self.rear  = None

    def enqueue(self, data):
        # node creation
        newnode = Node(data)
        # if front is None - set front to current node
        # rear point to new node
        if (self.front is None):
            self.front = newnode
        if (self.rear is not None):
            self.rear.next = newnode
        self.rear = newnode

    def dequeue(self):
        
        # delete front and return DeprecationWarning
        # front point to 2nd node

        if(self.rear is None): return 

        _temp = self.front
        _data = self.front.data

        if(self.front == self.rear):
            self.rear = None
        self.front = self.front.next

        del _temp
        return _data

    def printQueue(self):
        temp = self.front
        while(temp is not None):
            print(temp.data)
            temp = temp.next


q = Queue()
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

q.printQueue()

print( 'deleted: ', q.dequeue() )

q.printQueue()
