# https://leetcode.com/problems/find-unique-binary-string/
# backtracking
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # map the nums to a hashset
        strset = {num for num in nums}
        
        def backtrack(i, cur):
            # base case
            if i == len(nums):
                res = ''.join(cur)
                if res not in strset:
                    return res
                else:
                    return None
            
            # the decision can be '0'
            res = backtrack(i+1, cur)
            if res:
                return res
            
            # the decision can be '1'
            cur[i] = '1'
            res = backtrack(i+1,cur)
            if res:
                return res
           
            # start with all '0's
        return backtrack(0, ['0' for num in nums])