'''
author: Sharmila S
Date: 12-04-2021

Topic: Linear Search
'''

def linear_search(values, search_for):

    flag = 0 # holds the resut
    for i in range(0, len(values)):
        if(values[i] == search_for): # check whether equal to given value
            flag = 1  # elem is found
            break     # quit the loop
    
    if(flag):
        return True
    return False



arr = [64, 34, 25, 12, 22, 11, 90]
print(linear_search(arr, 12))
print(linear_search(arr, 91))