class Solution(object):
    def judgeSquareSum(self,input):
        if input < 0:
            return False
        left = 0
        right = int(input**0.5)
        while left <= right:
            temp = left * left + right * right
            if temp == input:
                return True
            elif temp > input:
                right -= 1
            elif temp < input:
                left += 1
        return False


input = 5
s = Solution()
print(s.judgeSquareSum(5))

# 双指针求解
# 右指针用平方根初始化，实现剪枝




