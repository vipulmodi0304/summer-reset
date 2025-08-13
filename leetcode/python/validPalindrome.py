#valid palindrome
#13th August 2025
#started doing two-pointers problems today. Didnt use two pointers for this one cuz its less efficient

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]