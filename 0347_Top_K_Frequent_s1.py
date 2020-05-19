from collections import Counter

class Solution(object):
    def topKFrequent(self,nums,k):
        # map = {}
        # for i in nums:
        #     map[i] = map.get(i,0) + 1    #生成字典映射
        map = Counter(nums) # 建立哈希表

        max_freq = max(map.values())
        bucket = [[] for _ in range(max_freq+1)] # 用列表推导式建立桶，因为同一频次可能有多个值
        for num, freq in map.items():
            bucket[freq].append(num) # 这里要用append，因为bucket[freq]是一个列表

        res = []
        for i in range(max_freq,0,-1): # 取前k频次
            if bucket[i]:
                res.extend(bucket[i]) # 这里要用extend，而不是append
            if len(res) >= k:
                return res[:k]


nums = [2,2,2,1,1,4,5,5,5,5]
# nums = [1,2]
k = 2
s = Solution()
print(s.topKFrequent(nums,k))

# 哈希表 + 桶排序的方法