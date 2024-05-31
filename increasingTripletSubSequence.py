# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

# Example 1:

# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
# Example 2:

# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.
# Example 3:

# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.



import sys
import math
from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if(nums == None and len(nums) < 3):
            return False
        
        min1 = 2**31 
        min2 = 2**31
        
        for i in nums:
            if i < min1:
                min1 = i
                
            if i > min1:
                min2 = i if i < min2 else min2
                
            if i > min2:
                return True
        
        return False
        
