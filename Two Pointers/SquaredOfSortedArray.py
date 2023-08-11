class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        l,r = 0,len(nums)-1
        w = len(nums)-1
        res = [None for _ in range(len(nums))]

        while w>=0:
            ls = nums[l]**2 
            rs = nums[r]**2 
            if ls > rs:
                res[w]= ls
                l+=1
            else:
                res[w]= rs
                r-=1
            w-=1
        return res