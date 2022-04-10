class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        max1 = float('-inf')
        max2 = float('-inf')

        for i in nums:
            max1 = max(i, max1+i)
            max2 = max(max1, max2)

        return max2
