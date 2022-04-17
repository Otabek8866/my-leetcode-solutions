class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        s = bin(n)[2:]
        return True if s[0] == '1' and s.count('1') == 1 else False
