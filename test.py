from collections import Counter
from heapq import *

class Solution(object):
    def topKFrequent(self,nums,k):
        map = Counter(nums)

        heap = []
        for num, freq in map.items():
            heappush(heap,(freq, num))
            if len(heap) > k:
                heappop(heap)

        result = []
        while heap:
            top = heappop(heap)
            result.append(top[1])

        return result[::-1]


nums = [2,2,2,1,1,4,5,5,5,5]
# nums = [1,2]
k = 2
s = Solution()
print(s.topKFrequent(nums,k))
