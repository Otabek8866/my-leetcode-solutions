class Solution:
    def hammingWeight(self, n: int) -> int:
        # bin() built-in func converts integer to string in 0b1011 (n=3)
        # count() finds how many times "1" occurs in the string
        return bin(n).count('1', 2)

        # solution 2
        # res = 0
        # while n:
        #     n &= n - 1
        #     res += 1
        # return res
