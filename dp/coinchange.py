# https://leetcode.com/problems/coin-change-2/
# leetcode 518
# medium
# dynamic program

# solution 1 memory of O(n*m)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        
        def dfs(i,a):
            if a == amount:
                return 1
            if a> amount:
                return 0
            if i == len(coins):
                return 0
            if (i,a) in cache:
                return cache[(i,a)]
            
            cache[(i,a)] = dfs(i+1,a)+dfs(i,a+coins[i])
            return cache[(i,a)]
        
        return dfs(0,0)


# solution 2, better memory of O(n)