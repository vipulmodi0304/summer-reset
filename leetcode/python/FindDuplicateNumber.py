#May 20th 2025
#Finding the Duplicate number
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        prev = {}
        for i in range(len(nums)):
            if nums[i] in prev:
                return nums[i]
            else:
                prev[nums[i]]=True
        return -1        
        