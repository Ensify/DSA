class Solution:
    def maxProduct(self, s: str) -> int:
        pali = {}

        for mask in range(1<<len(s)):
            sub = ""
            for i in range(len(s)):
                if mask & (1 << i):
                    sub += s[i]
            if sub == sub[::-1]:
                pali[mask] = len(sub)
        res = 0
        for i,a in pali.items():
            for j,b in pali.items():
                if i & j == 0:
                    res = max(res,a*b)
        return res