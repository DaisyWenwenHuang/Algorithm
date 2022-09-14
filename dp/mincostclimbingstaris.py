# https://leetcode.com/problems/min-cost-climbing-stairs/
# leetcode 746
# easy
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        
        for i in range(len(cost)-3,-1,-1):
            cost[i] += min(cost[i+1],cost[i+2])
			# return the min of [0] and [1] is because we can choose start from
			# index 0 or index 1
        return min(cost[0],cost[1])