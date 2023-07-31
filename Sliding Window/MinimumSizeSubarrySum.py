class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        m = float('inf')
        l = 0
        s = 0
        for i,a in enumerate(nums):
            s+=a
            while(s>=target):
                m = min(m,i+1-l)
                s-=nums[l]
                l+=1
        return int(m) if m!=float('inf') else 0