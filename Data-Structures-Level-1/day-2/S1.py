class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = 0
        for i in range(len(nums)-1):
            # assume the first number is nums[i], so we subtract this from "target"
            # and we search for the remainder
            num = target - nums[i]
            if num in nums[i+1:]:
                # if the remainder in nums, we'll return the indices
                return [i, nums.index(num, i+1)]
                # otherwise, we'll check with the next element

# Second Version


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         index = 0
#         for i in range(len(nums)-1):
# 		# assume the first number is nums[i], so we subtract this from "target"
# 		# and we search for the remainder
#             num = target - nums[i]
#             try:
# 		# if the remainder in nums, we'll return the indices
#                 index = nums.index(num, i+1)
#                 return [i, index]
#             except:
# 		# otherwise, we'll check with the next element
#                 continue
