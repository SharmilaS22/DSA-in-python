'''
author: Sharmila S
Date: 18-04-2021

Topic: Merge sort
'''

def MergeSort(arr):

    # Algorithm
    # divide into two half
    # and sort while merging 

    if ( len(arr) > 1 ): # if one elem return, no further split

        mid = len(arr) // 2 

        left = arr[:mid]
        right = arr[mid:]
        
        MergeSort(left)
        MergeSort(right)

        left_ind, right_ind, arr_index = 0, 0, 0

        while (left_ind < len(left) and right_ind < len(right)):

            if (left[left_ind] < right[right_ind] ):
                arr[arr_index] = left[left_ind]
                left_ind += 1
            else:
                arr[arr_index] = right[right_ind]
                right_ind += 1
            
            arr_index += 1

        if (left_ind < len(left)):
            arr[arr_index] = left[left_ind]
            arr_index += 1
            left_ind += 1
        else:
            arr[arr_index] = right[right_ind]
            arr_index += 1
            right_ind += 1

list1 = [3, 5, 2, 0, 13, 9, 6]

MergeSort(list1)

print(list1)