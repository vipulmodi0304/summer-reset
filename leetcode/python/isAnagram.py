#May 21st 2025
#isAnagram

#Notes: 1. Thought of using double loop to get through each character in s and compare with each char in t, but that would take too long.
#       2. So thought of using HashMap instead. I would store each char with their freq in 2 maps. If maps are equal, I would return true.
#       3. This problem didnt take too long and I was able to figure it out in 15 minutes


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        countS={}
        countT={}
        for char in s:
            countS[char]=countS.get(char,0)+1
        for char in t:
            countT[char]=countT.get(char,0)+1
        return countS==countT        
        g