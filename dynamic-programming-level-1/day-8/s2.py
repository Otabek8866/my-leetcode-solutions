class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        #         left = 0
        #         right = 1
        #         profit = 0
        #         total = 0
        #         l = len(prices)

        #         while right < l:
        #             if prices[right] > prices[left]:
        #                 cur = prices[right] - prices[left] - fee
        #                 if cur > 0:
        #                     profit = max(profit, cur)
        #                     if right < l-1 and prices[right+1]+fee < prices[right]:
        #                         left = right
        #                         total += profit
        #                         profit = 0
        #             else:
        #                 left = right
        #             right += 1
        #         total += profit
        #         return total

        # adopted from @Sirius930
        n = len(prices)
        if n < 2:
            return 0
        ans = 0
        minimum = prices[0]
        for i in range(1, n):
            if prices[i] < minimum:
                minimum = prices[i]
            elif prices[i] > minimum + fee:
                ans += prices[i] - fee - minimum
                minimum = prices[i] - fee
        return ans
