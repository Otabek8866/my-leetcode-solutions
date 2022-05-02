class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        total = 0
        count = 1
        num = nums[0] - nums[1]
        for i in range(2, len(nums)):
            diff = nums[i-1] - nums[i]
            if num == diff:
                count += 1
            else:
                num = diff
                if count > 1:
                    total += (count + 1)*(count - 2)//2 + 1
                    count = 1                
        if count > 1:
            total += (count + 1)*(count - 2)//2 + 1
            
        return total