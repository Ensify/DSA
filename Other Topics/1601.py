class Solution:
    def maximumRequests(self, n: int, requests: list[list[int]]) -> int:
        m = 0
        r = len(requests)
        for i in range(2**r):
            buildings = [0 for _ in range(n)]
            c = bin(i).count("1")
            if not c>m:
                continue
            k=0
            while i>0:
                if i&1:
                    buildings[requests[k][0]]-=1
                    buildings[requests[k][1]]+=1
                i=i>>1
                k+=1
            if all(v == 0 for v in buildings):
                m = c

        return m