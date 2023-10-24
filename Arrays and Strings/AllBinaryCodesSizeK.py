class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        s = set([s[i:i+k] for i in range(len(s)-k+1)])
        return len(s)==2**k