'''
author: Sharmila S
Date: 21-04-2021

Topic: Find h index
'''

def isHIndex(arr, num):
    great, equal = 0, 0
    for elem in arr:
        if (elem > num):    great += 1
        elif (elem == num): equal += 1

        if (great+equal >= num): return True


def hIndex(arr):
    maxH = -9999
    for i in range(min(arr), max(arr)+1):
        if (isHIndex(arr, i)):
            maxH = max(maxH, i)
    return maxH


list1 = [3, 0, 6, 1, 5]
print(hIndex(list1))