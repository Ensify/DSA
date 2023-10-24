class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        d = set()
        ans = []
        for i in range(len(s)-9):
            sub = s[i:i+10]
            if sub in d and sub not in ans:
                ans.append(sub)
            else:
                d.add(sub)
        return ans