class Solution:
    def validPartition(self, n: list[int]) -> bool:

        if len(n)<2: return False

        curr = n[0]==n[1]
        prev = False
        pprev = True
        for i in range(2,len(n)):
            ival = False

            if n[i]==n[i-1] and prev:
                ival = prev
            elif n[i]==n[i-1]==n[i-2] or n[i] == n[i-1]+1 == n[i-2]+2:
                ival = pprev
                       
            pprev,prev,curr=prev,curr,ival

        return curr

"""
class Solution:
    def validPartition(self, n: List[int]) -> bool:
        f,s,t=True,False,n[0]==n[1]
        for i in range(2,len(n)): f,s,t = s,t, s if n[i]==n[i-1] and s else f if n[i]==n[i-1]==n[i-2] or n[i]==n[i-1]+1==n[i-2]+2 else False
        return t
"""