# https://leetcode.com/problems/matchsticks-to-square/
# backtracking 
# similar to leetcode698
# example one not working
# [5,5,5,5,4,4,4,4,3,3,3,3]
# example two working
# [1,1,2,2,2]
# why?
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        k = 4
        total = sum(matchsticks)
        used = [False]*len(matchsticks)
        if total % 4 != 0:
            return False
        target = total // 4
        matchsticks.srot(reverse=True)
        
        def dfs(k,cursum,start):
            # base case
            if k == 0:
                return True

            while start < len(matchsticks):
                cursum += matchsticks[start]
                if cursum == target and not used[start]:
                    used[start] = True
                    return dfs(k-1,0,start+1)
                if cursum < target:
                    return dfs(k,cursum,start+1)
                
                if cursum > target:
                    used[start] = False
                    break
            return False
        
        return dfs(4,0,0)

# another solution . accepted
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        length = sum(matchsticks) // 4
        sides = [0] * 4
        
        if sum(matchsticks) / 4 != length:
            return False
        
        matchsticks.sort(reverse=True)
        
        def dfs(i):
            # base case
            if i == len(matchsticks):
                return True
            
            for j in range(4):
                if sides[j] + matchsticks[i] <= length:
                    sides[j] += matchsticks[i]
                    if dfs(i+1):
                        return True
                    sides[j] -= matchsticks[i]
            return False
        return dfs(0)
            