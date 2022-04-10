class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # counter = nums.count(0)
        # while True:
        #     if 0 in nums:
        #         nums.remove(0)
        #     else:
        #         break
        # nums += [0 for _ in range(counter)]
        left = 0
        while left < len(nums):
            if nums[left] == 0:
                break
            left += 1
        right = left + 1
        while right < len(nums):
            if nums[right] != 0:
                nums[left] = nums[right]
                nums[right] = 0
                left += 1
            right += 1
