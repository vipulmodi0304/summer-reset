#13th August 2025
#TwoSum part 2
# Use a single while loop; move only one pointer each step until target is found.
# Ensure all paths return before loop ends to avoid returning None.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers)-1
        while l<r:
            if numbers[l]+numbers[r]==target:
                return [l+1,r+1]
            elif numbers[l]+numbers[r]<target:
                l+=1
            else:
                r-=1     
        g