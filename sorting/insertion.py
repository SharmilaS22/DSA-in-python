'''
author: Sharmila S
Date: 18-04-2021

Topic: Insertion sort
'''

def InsertionSort(arr):

    # Algorithm
    # sort sub array
    # new elem is added into sorted array

    for i in range(1, len(arr)):

        key = arr[i]
        j = i-1
        while (j >= 0 and arr[j] > key):
            arr[j+1] = arr[j] # move one place to right
            j = j-1
        arr[j+1]  = key

    return


list1 = [3, 5, 2, 0, 13, 9, 6]

InsertionSort(list1)

print(list1)
