class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False
        mappings = {}
        for a,b in zip(s,t):
            if a not in mappings:
                if b in mappings.values(): return False
                mappings[a]=b
            else:
                if mappings[a]!=b:
                    return False
        return True