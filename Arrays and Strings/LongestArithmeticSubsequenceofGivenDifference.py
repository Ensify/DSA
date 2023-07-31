from collections import defaultdict
class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        mp=defaultdict(int)
        m=0
        for i in arr:
            mp[i]=mp[i-difference]+1
            m=max(mp[i],m)
        return m


