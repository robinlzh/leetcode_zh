class Solution(object):
    def validPalindrome(self, input_s):
        input = list(input_s)
        left = 0
        right = len(input) - 1
        while left <= right:
            if input[left] != input[right]:
                case1 = input[left:right]
                case2 = input[left+1:right+1]
                return case1 == case1[::-1] or case2 == case2[::-1]
            left += 1
            right -= 1
        return True

input = "abcda"
s = Solution()
print(s.validPalindrome(input))

# 如果不等，要么删除右边case2，要么删除左边case1
