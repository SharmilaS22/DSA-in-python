'''
author: Sharmila S
Date: 18-04-2021

Topic: Queue
'''

class Queue:

    def __init__(self):
        self.queue = []
        self.front = -1
        self.rear  = -1

    def enqueue(self, data):
        self.queue.append(data)
        if (self.front == -1):
            self.front = 0
        self.rear += 1
    
    def dequeue(self):
        self.queue