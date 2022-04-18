class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for i in range(0, len(nums)-1, 2):
            if nums[i] != nums[i+1]:
                return nums[i]
        return nums[-1]

        # Solution 2
        # res = 0
        # for i in nums:
        #     res ^= i
        # return res
