class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if (len(nums) == 1):
            nums = nums
        
        length = len(nums)
        
        for i in range(0, length):
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.append(0)
