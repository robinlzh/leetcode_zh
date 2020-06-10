class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        child = 0
        cookie = 0
        while child < len(g) and cookie < len(s):
            if g[child] <= s[cookie]:
                child += 1
            cookie += 1
        return child


solution = Solution()
g = [1, 2]
s = [1, 2, 3]
print(solution.findContentChildren(g, s))