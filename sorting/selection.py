'''
author: Sharmila S
Date: 18-04-2021

Topic: Selection sort
'''

def SelectionSort(arr):

    #  for n values
    #  find min element in i+1 to n
    #  add the min elemnt (ith smallest) to ith position
    n = len(arr)
    for i in range(0, n):

        minval = arr[i] # first elem as min val
        minindex= i

        # find min elem index in arr[i+1:]
        for j in range(i+1, n):
            if(minval > arr[j]):
                minindex = j
                minval = arr[j]
        
        # swapping
        arr[i], arr[minindex] = arr[minindex], arr[i]

    return


list1 = [2, 8, 3, 9, 1, 4]

SelectionSort(list1)

print(list1)