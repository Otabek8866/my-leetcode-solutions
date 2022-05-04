class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        i = j = k = 0
        while n > 1:
            a, b, c = nums[i]*2, nums[j]*3, nums[k]*5
            num = min((a, b, c))
            if num == a:
                i += 1
            if num == b:
                j += 1
            if num == c:
                k += 1
            nums.append(num)
            n -= 1
        return nums[-1]

