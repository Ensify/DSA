from collections import defaultdict

class Solution:
    def leastBricks(self, wall: list[list[int]]) -> int:
        gaps = defaultdict(int)
        gaps[0]=0

        for row in wall:
            tot_width = 0
            for brick in row[:-1]:
                tot_width+=brick
                gaps[tot_width]+=1
                
        return len(wall)-max(gaps.values())