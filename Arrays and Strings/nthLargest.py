class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:

        def partition(l,r):
            p = nums[r]
            s = l
            for i in range(l,r):
                if nums[i]<p:
                    nums[i],nums[s]=nums[s],nums[i]
                    s+=1
            nums[r],nums[s]=nums[s],nums[r]
            return s
        
        l =0
        r = len(nums)-1
        
        while True:
            p = partition(l,r)
            if len(nums)-k ==p:
                return nums[p]
            elif len(nums)-k>p:
                l=p+1
            else:
                r=p-1