class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # code is adopted from @lee215
        B = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            B[i] *= B[i - 1] or 1
            print(nums)
            print(B)
        return max(nums + B)

