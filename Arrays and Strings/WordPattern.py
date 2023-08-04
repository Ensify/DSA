class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        mapping = {}
        if len(s)!= len(pattern): return False

        for i,a in enumerate(pattern):
            if a in mapping:
                if mapping[a]!=s[i]:
                    return False
            if a not in mapping:
                if s[i] in mapping.values(): return False
                mapping[a] = s[i]
        
        return True
