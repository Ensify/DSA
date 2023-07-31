class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = dict(zip("balon",[0,0,0,0,0]))
        for i in text:
            if i in d:
                d[i]+=1
        m = min(2*d["b"],2*d["a"],d["l"],d["o"],2*d["n"])
        return m//2