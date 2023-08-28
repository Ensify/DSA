class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        force = [0 for _ in range(n)]
        f=0
        for i in range(n):
            if dominoes[i]=="R":
                f=n
            elif dominoes[i]=="L":
                f=0
            else:
                if f>0: f-=1
            force[i]+=f
        
        f=0
        for i in range(n-1,-1,-1):
            if dominoes[i]=="R":
                f=0
            elif dominoes[i]=="L":
                f=n
            else:
                if f>0: f-=1
            force[i]-=f
        
        ans = ["." if f==0 else "L" if f<0 else "R" for f in force]
        return "".join(ans)
        