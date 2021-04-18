'''
author: Sharmila S
Date: 18-04-2021

Topic: Bubble sort
'''

def BubbleSort(arr):
    # Algorithm
    # for n times
    # take two elems and swap their pos when not in ascending
    n = len(arr)
    for i in range(n-1):
        
        for j in range(i+1, n):

            if (arr[i] > arr[j]):
                # swapping
                arr[i], arr[j] = arr[j], arr[i]

    return

    


list1 = [1, 8, 2, 5, 3, 10]
BubbleSort(list1)

print(list1)

