#19th May 2025
#Two Sum
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {}
        for i,n in enumerate(nums):
          diff = target - n
          if diff in prevMap:
            return(prevMap[diff], i)
          prevMap[n] = i
 


solution = Solution()
print(solution.twoSum([3,4,5,6,7], 8))
    
    
          