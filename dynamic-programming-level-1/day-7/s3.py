class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        profit = 0
        total = 0
        l = len(prices)

        while right < l:
            if prices[right] > prices[left]:
                cur = prices[right] - prices[left]
                profit = max(profit, cur)
                if right < l-1 and prices[right+1] < prices[right]:
                    left = right
                    total += profit
                    profit = 0
            else:
                left = right
            right += 1
        total += profit
        return total

        # total = 0
        # for i in range(1, len(prices)):
        #     if prices[i] > prices[i-1]:
        #         total += prices[i] - prices[i-1]
        # return total
