# https://leetcode.com/problems/combination-sum/
# backtracking
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dsf(i,curcomb,cursum):
            # base case
            if cursum == target:
                res.append(curcomb.copy())
                return
            if cursum > target or i >= len(candidates):
                return
            
            # main function
            # first decision: including [i]
            curcomb.append(candidates[i])
            dsf(i,curcomb,cursum + candidates[i])
            
            curcomb.pop()
            # second decision : not including the [i]
            dsf(i+1,curcomb,cursum)
            
        
        dsf(0,[],0)
        return  res