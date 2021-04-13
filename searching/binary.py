'''
author: Sharmila S
Date: 13-04-2021

Topic: Binary Search
'''

def binary_search(arr, first, last, val):

    if(first > last):
        return None, False 

    mid = (first+last)//2

    for i in range(first, last+1):
        if( arr[mid] == val):
            return i, True
        if( arr[mid] > val ):
            return binary_search(arr, first, mid-1, val)
        else:
            return binary_search(arr, mid+1, last, val)


list1 = [1, 2, 6, 7, 8, 10, 12] # sorted order

print(binary_search(list1, 0, len(list1)-1, 4)) # None, False
print(binary_search(list1, 0, len(list1)-1, 6)) # 4,    True