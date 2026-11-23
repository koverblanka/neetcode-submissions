class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 2:
            return min(cost[0], cost[1])

        penult_cost = 0
        last_cost = 0

        for i in range(2, len(cost)+1):
            curr_cost = min(penult_cost + cost[i-2], last_cost + cost[i-1])

            penult_cost = last_cost
            last_cost = curr_cost
        
        return curr_cost