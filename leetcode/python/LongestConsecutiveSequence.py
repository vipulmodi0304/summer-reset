#28th May 2025
#Longest Consecutive Sequence
#Took a break from problems. Now will solve them daily. for this problem didnt know how to keep note of curr count and best count so used chatgpt to get the idea. 
#Solve again

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       if not nums:
        return 0
       num_set = set(nums)
       longest = 0

       for x in num_set:
        if x-1 not in num_set:
            length = 1
            while x+length in num_set:
                length+=1
            longest = max(longest,length)
       return longest              
        