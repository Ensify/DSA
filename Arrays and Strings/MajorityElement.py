class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        maj = None
        count = 0
        for i in nums:
            if not count: maj = i
            if i == maj: count+=1
            else: count-=1
        return maj