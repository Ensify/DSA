class Solution:
    def numDecodings(self, s: str) -> int:
        a,b = 1,1

        for i in range(len(s)-1,-1,-1):

            if s[i]=="0":
                t=0
            else:
                t = a

            if i+1 < len(s) and 9<int(s[i:i+2])<27:
                t += b

            a,b = t,a

        return a
            