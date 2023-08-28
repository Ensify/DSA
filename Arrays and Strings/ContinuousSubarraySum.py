class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        d = {0:-1}
        s = 0
        for i,a in enumerate(nums):
            s+=a
            if s % k not in d:
                d[s % k] = i
            elif d[s % k] < i-1:
                return True

        return False