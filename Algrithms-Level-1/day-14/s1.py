class Solution:
    def reverseBits(self, n: int) -> int:
        return int("{:032b}".format(n)[::-1], 2)

# solution 2
    # def reverseBits(self, n):
    #     ans = 0
    #     for i in xrange(32):
    #         ans = (ans << 1) + (n & 1)
    #         n >>= 1
    #     return ans
