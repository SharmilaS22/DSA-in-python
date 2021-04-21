'''
author: Sharmila S
Date: 20-04-2021

Topic: Queue using stack
'''

class Stack:
    
    def __init__(self):
        self.stack = []
        self.top   = -1

    def push(self, data):
        self.stack.append(data)
        self.top += 1
    
    def pop(self):
        if( self.top > -1 ):
            self.top -= 1
            return self.stack.pop()
        
    def getTop(self):
        return self.stack[self.top]
        
    def printstack(self):
        print(self.stack)
    
s1 = Stack()
s2 = Stack()

# querytype 1 - enqueue the data
# type 2 = dequeue
# type 3 - print front element

queries = [
    [1, 3],
    [2],
    [1, 5],
    [1, 4],
    [1, 7],
    [3],
    [2],
    [3]
]

for q in queries:
    
    if ( q[0] == 1 ):
        # enqueue
        # 1
        for _ in range(0, s1.top+1):
            s2.push(s1.pop())
          
        s1.push(q[1])
        
        for _ in range(0,s2.top+1):
            s1.push(s2.pop())
        
    elif ( q[0] == 2 ):
        # dequeue
        s1.pop()
    
    else:
        # print front element
        print(s1.getTop())
    
    # s1.printstack()

