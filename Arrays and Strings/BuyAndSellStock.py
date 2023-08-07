class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        p = prices[0]
        for v in prices:
            if v>p:
                res+=v-p
            p=v
        return res