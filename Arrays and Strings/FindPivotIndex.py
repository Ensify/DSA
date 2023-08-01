class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        right = sum(nums)
        left = 0

        for i,a in enumerate(nums):
            if left==right-a:
                return i
            left+=a
            right-=a
        return -1