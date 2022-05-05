# https://leetcode.com/problems/permutations-ii/
# foolow up  of th permutation problem. the difference is this one 
# might contain depulicate numbers
# aka : result need to filter out the depulicate ones.
# permutation code update
# need a hashmap to track results
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
		# get all the unique nums in the list
        count = {n:0 for n in nums}
		# count numbers
        for n in nums:
            count[n] += 1
        
        def dfs():
			# base case
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for n in count:
                if count[n]> 0:
                    perm.append(n)
                    count[n] -= 1
                    
                    dfs()
                    # each dsf() has the two codes below that made sure to back tack to the node above
                    count[n] += 1
                    perm.pop()
        dfs()
        return res
   