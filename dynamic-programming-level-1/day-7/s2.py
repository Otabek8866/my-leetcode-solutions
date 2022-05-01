class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_pt = 0
        right_pt = 1
        profit = 0

        while right_pt < len(prices):
            curr = prices[right_pt] - prices[left_pt]
            if prices[right_pt] > prices[left_pt]:
                profit = max(profit, curr)
            else:
                left_pt = right_pt
            right_pt += 1

        return profit
