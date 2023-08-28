class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        c = False
        for i in range(len(nums)):
            if i==0:
                continue
            if nums[i]<nums[i-1]:
                if c:
                    return False
                if i==1 or nums[i] >= nums[i - 2]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
                c=True
        return True
