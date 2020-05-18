class Solution(object):
    def partition(self,nums,low,high):
        i = low - 1
        pivot = nums[high]
        for j in range(low,high):
            if nums[j] >= pivot: # 注意是大于，求第k大的，所以是倒着排
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1], nums[high] = nums[high], nums[i+1]
        return i+1

    def findKthLargest(self,nums,k):
        low = 0
        high = len(nums) - 1
        while True:
            pi = self.partition(nums,low,high)
            if pi == k-1:
                return nums[pi]
            elif pi < k-1:
                low = pi + 1
            else:
                high = pi - 1


nums = [3,2,1,5,6,4]
k = 2
s = Solution()
print(s.findKthLargest(nums,k))
