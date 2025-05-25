#24th May 2025
#TopKFrequentElements


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         prev = {}
         for num in nums:
            if num in prev:
                prev[num]+=1
            else:
                prev[num]=1

         freq_sorted = sorted(prev.items(), key=lambda x:x[1], reverse = True)

         result = []
         for items, freq in freq_sorted[:k]:
            result.append(items)

         return result                

        