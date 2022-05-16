# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
# backtracking
# sort or not?
# descending order to save some cal time as one of the condition is cur> target
# the solution below trigger time limit exceeded error but it is a legit solution
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # nums.sort(reverse = True)
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
            
            for j in range(i,len(nums)):
                if used[j] or cursum + nums[j] > target:
                    continue
                used[j] = True
                if backtrack(j+1,k, cursum + nums[j]):
                    return True
                # clean up 
                used[j] = False
            return False
        return backtrack(0,k,0)

#  other solutions
		# still time limite exceeded
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total,n = sum(nums),len(nums)
        if total % k != 0:
            return False
        partsum = total // k
        
        visited = [False]* n 
        nums.sort(reverse = True)
        def dfs(kleft, i , cursum):
            if kleft == 0:
                return True
            if cursum == partsum:
                return dfs(kleft-1,0,0)
            
            for j in range(i,n):
                if not visited[j] and cursum + nums[j]<=partsum:
                    visited[j]= True
                    if dfs(kleft,j+1,cursum+nums[j]):
                        return True
                    visited[j]=False
            return False
        
        return dfs(k,0,0)


