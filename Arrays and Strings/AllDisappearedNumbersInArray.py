class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for i,a in enumerate(nums):
            nums[abs(a)-1] = -(abs(nums[abs(a)-1]))

        return [i+1 for i,a in enumerate(nums) if a>0]