class Solution:
    def partitionString(self, s: str) -> int:
        res = 0
        sub = ''

        for i in s:

            if i in sub:
                res+=1
                sub = i
            else:
                sub+=i
        
        if sub:
            res+=1
        
        return res