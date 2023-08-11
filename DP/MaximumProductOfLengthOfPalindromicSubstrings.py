from functools import cache


class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        @cache
        def findMax(s):
            if not s:
                return 0
            n = len(s)
            if n == 1:
                return 1
            res = max(findMax(s[1:]), findMax(s[:-1]))
            if s[0] == s[-1]:
                res = max(res, 2 + findMax(s[1:-1]))
            return res
        @cache
        def dp(idx, s1, s2):
            if idx == n:
                return findMax(s1) * findMax(s2)
            return max(dp(idx + 1, s1 + s[idx], s2), dp(idx + 1, s1, s2 + s[idx]))
        return dp(0, '', '')

