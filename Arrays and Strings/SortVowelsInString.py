class Solution:
    def sortVowels(self, s: str) -> str:
        l = list(s)
        v = []
        for i,a in enumerate(l):
            if a.lower() in "aeiou":
                v.append(a)
        v.sort()
        k=0
        for i,a in enumerate(l):
            if a.lower() in "aeiou":
                l[i] = v[k]
                k+=1


        return "".join(l)
