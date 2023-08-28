from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        k=len(p)
        res = []

        d = defaultdict(int)
        for i in p: d[i]+=1

        window = defaultdict(int)
        for i in s[:k]: window[i]+=1

        for i in range(len(s)-k):
            if window==d:
                res.append(i)
            window[s[i]]-=1
            if window[s[i]]==0:
                del window[s[i]]
            window[s[i+k]]+=1

        if window.items()==d.items():
            res.append(len(s)-k)
            
        return res