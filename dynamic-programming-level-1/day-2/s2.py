class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        p = [cost[0], cost[1]]
        for i in range(2, len(cost)):
            p.append(cost[i] + min(p[i-1], p[i-2]))
        return min(p[-2], p[-1])
