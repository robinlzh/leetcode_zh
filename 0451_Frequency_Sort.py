from collections import Counter
from heapq import *

class Solution(object):
    def frequencySort(self,string):
        letters = list(string)
        map = Counter(letters)

        heap = []
        for lett, freq in map.items():
            heappush(heap, (freq,lett))

        result = []
        while heap:
            top = heappop(heap)
            result.append(top[0]*top[1])
        return "".join(result[::-1])


string = "Aabb"
s = Solution()
print(s.frequencySort(string))