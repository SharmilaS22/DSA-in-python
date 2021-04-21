'''
author: Sharmila S
Date: 21-04-2021

Topic: Stack using Queue
'''

# local imports
import sys
sys.path.append(r"D:\sharmi-projects\DSA_py")

from queues.queueLL import Queue

# Algorithm
# two queues
# q1 - empty always
# q2 - stack

# add elem to q1
# dequeue everything from q2 and add it to q1
# swap q2, q1


class StackUsingQueues:

    def __init__(self) -> None:
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, _data):
        self.q1.enqueue(_data)

        while(self.q2.rear is not None):
            self.q1.enqueue(self.q2.dequeue())
        
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):

        return self.q2.dequeue()

    def printStack(self):
        self.q2.printQueue()
        return

stack = StackUsingQueues()

stack.push(2)
stack.push(3)
stack.push(4)

stack.printStack()

stack.pop()

stack.printStack()

