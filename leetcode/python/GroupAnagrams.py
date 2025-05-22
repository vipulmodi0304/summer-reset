#May 21st 2025
#Group Anagrams

#notes: 1. COuld not solve on own. Saw the solution andd then did it. I was confused about how strings, lists and hashmaps would work together. 
      # 2. asked chatgpt to make a cheatsheet for arrays/hashmaps problems which I found quite useful. Currently learning hashmaps in detail to avoid further problems.
      # 3. sorted sorts strings and returns them as a list of sorted characters.


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}  # Key = sorted string, Value = list of words

        for word in strs:
            # Step 1: Sort the word and use it as a key
            sorted_word = "".join(sorted(word))

            # Step 2: Add the original word to the group
            if sorted_word in anagram_map:
                anagram_map[sorted_word].append(word)
            else:
                anagram_map[sorted_word] = [word]

        # Step 3: Return all the grouped anagram lists
        return list(anagram_map.values())
