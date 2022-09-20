# https://leetcode.com/problems/maximum-subarray/
# leetcode 53
# medium
# greedy
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
		# maxsum can not be 0 as there is negative numbers in the list
        maxsum = nums[0]
        cursum = 0
        for n in nums:
			# whenever the prefix is negative, reset cursum to 0
            if cursum <0 :
                cursum = 0
            cursum += n
            maxsum = max(maxsum,cursum)
        return maxsum