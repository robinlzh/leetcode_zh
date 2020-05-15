class Solution(object):
    def twoSum(self,numbers,target):
        left = 0
        right = len(numbers) - 1
        while left < right:
            temp = numbers[left] + numbers[right]
            if temp == target:
                return [left+1, right+1]
            elif temp > target:
                right -= 1
            elif temp < target:
                left += 1


numbers = [5,25,75]
target = 100
s = Solution();
print(s.twoSum(numbers, target))
