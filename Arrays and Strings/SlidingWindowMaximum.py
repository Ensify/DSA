from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q = deque()
        res = []

        for i in range(k):
            while q and nums[i]>=nums[q[-1]]:
                q.pop()
            q.append(i)
        res.append(nums[q[0]])

        for i in range(k,len(nums)):
            if q and q[0] == i-k:
                q.popleft()
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            
            q.append(i)
            res.append(nums[q[0]])
            
        return res