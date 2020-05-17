class Solution(object):
    def merge(self,nums1,m,nums2,n):
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                # nums1[p] = nums1[p1]
                nums1[p], nums1[p1] = nums1[p1], nums1[p] # swap更容易理解
                p1 -= 1
            p -= 1
        nums1[:p2+1] = nums2[:p2+1]
        # 因为nums1中比nums2大的都往后移了
        # 所以如果nums2中有剩余，可以直接放在nums1中
        return nums1

nums1 = [2,4,6,0,0,0,0]
m = 3
nums2 = [1,3,5,7]
n = 4
s = Solution()
print(s.merge(nums1,m,nums2,n))
