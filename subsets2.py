# https://leetcode.com/problems/subsets-ii/
# backtracking
   res = []
        nums.sort()
        
        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
				# res.append(subset.copy())
                return 
            
            # all subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i+1,subset)
            
            subset.pop()
            # all subsets that dont include nums[i]
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i + 1, subset)
            
        backtrack(0,[])
        return res
# accepted 