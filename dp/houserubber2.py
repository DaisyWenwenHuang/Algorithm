# https://leetcode.com/problems/house-robber-ii/
# leetcode 213
# medium
# basically just reusing house robber 1 in a clever way
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
            
        def helper(nums):
            rob1,rob2 = 0,0
            for m in nums:            
                temp = max(rob1+m,rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        
        return max(nums[0],helper(nums[1:]),helper(nums[:-1]))
        