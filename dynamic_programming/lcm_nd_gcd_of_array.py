'''
author: Sharmila S
Date: 20-04-2021

Topic: LCM and GCD of array of elements
'''

def gcd(arr):
    if(len(arr) == 1):  return arr[0]
    
    if ( len(arr) == 2 ):
        small = min(arr[0], arr[1])
        for i in range(1, small+1):
            if ( arr[0] % i == 0 and arr[1] % i == 0 ):
                gcd_two = i
        return gcd_two

    # return a list with first elem, and gcd of remaining elements
    return gcd( [ arr[0], gcd(arr[1:]) ])

def lcm(arr):

    if(len(arr) == 1):  return arr[0]
    
    if ( len(arr) == 2 ):
        return (arr[0]*arr[1]) // gcd(arr)
    
    return lcm( [arr[0], lcm(arr[1:]) ])
    
list1 = [3, 6, 18]

print('list: ', list1)
print('lcm is ', lcm(list1))
print('gcd is ', gcd(list1))

