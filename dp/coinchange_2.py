# https://leetcode.com/problems/coin-change/
# leetcode 322
# 1-d dp
# memorization 
# medium
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float(inf)]*(amount+1)
        dp[0] = 0
        for a in range(1,amount+1):
            for c in coins:
                if a-c >= 0:
                    dp[a] = min(dp[a],1+dp[a-c])
					# coin = 4
					# a = 7
					# dp[7] = 1+dp[3]
        if dp[amount] != float(inf):
            return dp[amount]
        else:
            return -1