'''
author: Sharmila S
Date: 30-04-2021

Topic: Deletion inplace
'''
# local imports
import sys
sys.path.append(r"D:\sharmi-projects\DSA_py")


def removeDupplicatesInplace(arr):

    if (arr == []):
        return arr
    
    writePointer = 1

    # check for distinct elements
    # add to the array from start using writepointer
    # readPointer to traverse through array 
    for readPointer in range(1, len(arr)):

        if (arr[readPointer] != arr[readPointer-1]):
            # distinct element
            arr[writePointer] = arr[readPointer]
            writePointer += 1
    
    # delete rem elements
    while (len(arr) > writePointer):
        arr.pop()


list1 = [0, 1, 1, 2, 3, 3, 5]

print(list1)
removeDupplicatesInplace(list1)
print(list1)