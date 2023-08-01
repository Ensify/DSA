class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        R = len(grid)
        C = len(grid[0])
        visited = set()
        ans = 0
        moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        def dfs(r,c):
            visited.add((r,c))
            for i,j in moves:
                if 0<= r+i <R and 0<=c+j <C and grid[r][c]=="1" and (r+i,c+j) not in visited:
                    dfs(r+i,c+j)
        
        for i in range(R):
            for j in range(C):
                if (i,j) not in visited and grid[i][j] == "1":
                    dfs(i,j)
                    ans+=1

        return ans