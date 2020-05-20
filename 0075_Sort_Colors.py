class Solution(object):
    def sortColors(self, nums):
        p0 = curr = 0
        p2 = len(nums) - 1
        while curr <= p2: # 必须取到等号
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[p2], nums[curr] = nums[curr], nums[p2]
                p2 -= 1
            else:
                curr += 1


nums = [2,0,1]
s = Solution()
s.sortColors(nums)
print(nums)
