# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
# backtracking
# sort or not?
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # nums.sort()
        target = sum(nums)/k
        used = [False]*len(nums)
        # edge case
        if target != int(target):
            return False
        
        def backtrack(i, k, cursum):
            # base case
            if k == 0:
                return True
            if cursum == target:
                return backtrack(0,k-1,0)
            
            for j in range(len(nums)):
                if used[j] or cursum + nums[j] > target:
                    continue
                used[j] = True
                if backtrack(j+1,k, cursum + nums[j]):
                    return True
                # clean up 
                used[j] = False
            return False
        return backtrack(0,k,0)