class NumArray:
    def __init__(self, nums: list[int]):
        self.nums= nums
        self.pre = []
        s = 0
        for i in nums:
            s+=i
            self.pre.append(s)
        print(self.pre)

    def sumRange(self, left: int, right: int) -> int:
        return self.pre[right]-(self.pre[left-1] if left else 0)
        