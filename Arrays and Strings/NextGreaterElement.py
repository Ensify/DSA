class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = []
        for i in nums1:
            for j in range(nums2.index(i),len(nums2)):
                if nums2[j]>i:
                    res.append(nums2[j])
                    break
            else:
                res.append(-1)
        return res