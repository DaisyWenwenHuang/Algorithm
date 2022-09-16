# https://leetcode.com/problems/house-robber-ii/
# leetcode 213
# medium
# see house robber one first
# basically just reusing house robber 1 in a clever way
# since we can not rob the first and the last house at the same time
# we can just split to two sub problems. one is not including the last house
# the other is not including the first house
# one edge case is there only one house, which is the frist and the last at the same time
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
        