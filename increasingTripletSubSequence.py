import sys
import math

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if(nums == None and len(nums) < 3):
            return false
        
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
        
