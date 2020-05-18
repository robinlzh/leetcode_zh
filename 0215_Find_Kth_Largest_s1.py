import heapq

class Solution(object):
    def findKthLargest(self,nums,k):
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

# 利用小顶堆的构造和弹出来得到Kth Largest Element
# 构造k个元素的堆，时间复杂度为O(logk)，nums中n个元素，因此总的时间复杂度是O(nlogk)
# 借助辅助空间存储堆，因此空间复杂度为O(k)
