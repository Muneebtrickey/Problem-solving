"""
Example 2: 2248. Intersection of Multiple Arrays

Given a 2D array nums that contains n arrays of distinct integers,
 return a sorted array containing all the numbers that appear in all n arrays.

For example, given nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]], return [3, 4].
 3 and 4 are the only numbers that are in all arrays.

"""

# approch 1 brute force approch

from typing import List

def common_elements_in_sortedform(nums :List[List[int]]) -> List[int]:

    array1 = nums[0]
    common = []
    n = len(nums)

    for num in array1:
        for i in range(1,n):
            if num not in nums[i]:
                break
        
            
            if i == n-1:
                common.append(num)
    
    return common


print(common_elements_in_sortedform([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]))



# approch 2
# using dictionary to solve this problem
from collections import defaultdict

def intersection(nums):
    counts = defaultdict(int)
    n = len(nums)
    common = []

    for array in nums:
        for num in array:
            counts[num] += 1
    

    for num in nums[0]:
        if counts[num] == n:
            common.append(num)
    
    return common


print(intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]))