class Solution:
    def gcd(self,m,n):
        return m if not n else self.gcd(n, m%n)

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2!=str2+str1: return ""
        return str1[:self.gcd(len(str1),len(str2))]