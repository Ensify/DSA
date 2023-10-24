class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        R,C = len(matrix),len(matrix[0])
        self.pre = [[0 for _ in range(C)] for _ in range(R)]

        for r in range(R):
            s = 0
            for c in range(C):
                s+=matrix[r][c]
                above = self.pre[r-1][c] if r!=0 else 0
                self.pre[r][c] += s + above
        print(*self.pre,sep="\n")

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.pre[row2][col2]
        ans -= self.pre[row1-1][col2] if row1>0 else 0
        ans -= self.pre[row2][col1-1] if col1>0 else 0
        ans += self.pre[row1-1][col1-1] if row1>0 and col1>0 else 0
        return ans