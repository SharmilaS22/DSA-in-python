'''
author: Sharmila S
Date: 17-04-2021

Topic: Stack 
'''

class Stack:

    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self, data):
        self.stack.append(data)
        self.top += 1

    def pop(self):
        self.top -= 1
        return self.stack.pop()

    def print(self):
        for i in range(self.top, 0, -1):
            print(self.stack[i], '-->', end="")
        print(self.stack[0])



stack = Stack()
stack.push(2)
stack.push(3)
stack.push(4)

print(stack.top)

# print(stack.pop())
stack.print()
# print(stack.top)