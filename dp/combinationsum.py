# https://leetcode.com/problems/combination-sum/
# leetcode 39
# medium
# return unique combinations 
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        i,j = 0,0
        
        def dfs(i,cur,total):
            if total == target:
                res.append(cur.copy())
                return 
            if i >=len(candidates) or total > target:
                return

			# two desitions , one to include [i] and one is not
			# the time complexity is O(2^h) where h is the height of the decision tree 
            cur.append(candidates[i])
            dfs(i,cur,total+candidates[i])
			# this code below is to clean up the cur before do the second decision (not including [i])
            cur.pop()
            dfs(i+1,cur, total)
            
        dfs(0,[],0)
        return res