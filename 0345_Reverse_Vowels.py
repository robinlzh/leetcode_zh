class Solution(object):
    def reverseVowels(self, input_s):
        input = list(input_s)
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        left = 0
        right = len(input) - 1
        while left < right:
            while (left<len(input)-1) and (input[left] not in vowel):
                left += 1
            while (right>0) and (input[right] not in vowel):
                right -= 1
            if (left<right) and (input[left] != input[right]):
                input[left], input[right] = input[right], input[left]
            left += 1
            right -= 1
        return "".join(input)


input = "hello"
s = Solution()
print(s.reverseVowels(input))
