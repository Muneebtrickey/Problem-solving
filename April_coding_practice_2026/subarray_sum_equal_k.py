"""
Example 4: 560. Subarray Sum Equals K

Given an integer array nums and an integer k,
 find the number of subarrays whose sum is equal to k.
"""

from collections import defaultdict

def subarray_sum(nums,k):
    counts = defaultdict(int)
    counts[0] = 1
    # store the prefix sum upto i
    curr = 0 
    ans = 0 

    for num in nums:
        curr += num
        ans += counts[curr - k]
        counts[curr] += 1
    

    return ans


nums = [1, 2, 1, 2, 1]
k = 3
print(subarray_sum(nums, k))