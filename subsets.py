# https://leetcode.com/problems/subsets/
# dfs
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        subset=[]
        def dsf(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # decision to include nums[i]
            subset.append(nums[i])
            dsf(i + 1)
            
            # desicion not to include nums[i]
            subset.pop()
            dsf(i + 1)
            
        dsf(0)
        return res