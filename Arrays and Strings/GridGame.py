class Solution:
    def gridGame(self, grid: list[list[int]]) -> int:
        
        ans = float("inf")
        l,r = 0,sum(grid[0])

        for a,b in zip(grid[0],grid[1]):
            r -= a
            ans = min(ans,max(l,r))
            l += b
        
        return ans