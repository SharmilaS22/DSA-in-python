'''
author: Sharmila S
Date: 19-04-2021

Topic: Find subset
'''

import itertools
from itertools import combinations

# Complete the maxSubsetSum function below.
def findSubset(arr):
    all_subsets = []
    for i in range(1, len(arr)+1):
        subsets = list(map(list, combinations(arr, i)))
        all_subsets.extend(subsets)
    
    return all_subsets

print(findSubset([2, 3, 4]))