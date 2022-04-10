class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(len(numbers)-1):
        #     k = target - numbers[i]
        #     if k in numbers[i+1:]:
        #         return [i+1, numbers.index(k, i+1)+1]
        # ++++++++++++++++++++++++++++++++++++++++++++++++++
        # for i in range(len(numbers)-1, 0, -1):
        #     if numbers[i] > target and target > 0:
        #         continue
        #     k = target - numbers[i]
        #     if k in numbers[0:i]:
        #         return [numbers.index(k, 0, i)+1, i+1]
        # ++++++++++++++++++++++++++++++++++++++++++++++++
        i = 0
        j = len(numbers) - 1
        while i < j:
            n = numbers[i] + numbers[j]
            if n == target:
                return [i+1, j+1]
            if n < target:
                i += 1
            else:
                j -= 1
