# Given two integer arrays nums1 and nums2, return an array of their intersection. \
#Each element in the result must appear as many times as it shows in both arrays and you 
#may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

from typing import List
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # n = len(nums1)
        # m = len(nums2)
        # out = []

        # if m > n:
        #     small = nums1
        #     big = nums2
        # else:
        #     small = nums2
        #     big = nums1

        # for i in range(len(small)):
        #     if small[i] in big:

        #         if small[i] not in out:
        #             out.append(small[i])

        # return out

        return (Counter(nums1)&Counter(nums2)).elements()