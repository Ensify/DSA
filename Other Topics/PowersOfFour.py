class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<0:
            return False
        bits = str(bin(n))[2:]
        if bits.count('1') == 1 and bits[::-1].find('1') % 2 == 0:
            return True
        return False
        