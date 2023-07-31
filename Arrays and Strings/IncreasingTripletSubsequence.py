class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        a = float('inf')
        b = float('inf')
        for i in nums:
            if i<=a:
                a=i
            elif i<=b: 
                b=i
            else:
                return True
        return False