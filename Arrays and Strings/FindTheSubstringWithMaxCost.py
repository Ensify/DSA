class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: list[int]) -> int:
        costs = {}
        for i,a in enumerate(chars):
            costs[a] = vals[i]
        for i in range(ord("a"),ord("z")+1):
            if chr(i) not in costs:
                costs[chr(i)] = i-ord("a")+1
        m = 0
        c = 0
        for i in s:
            c+=costs[i]
            if c<0:
                c = 0
            if c>m:
                m = c
        return m