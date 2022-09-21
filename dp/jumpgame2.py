# https://leetcode.com/problems/jump-game-ii/
# leetcode 45
# medium
# greedy
class Solution:
    def jump(self, nums: List[int]) -> int:
		# l,r is the window of how far can be reached from last window/jump
        l,r = 0,0
        n = len(nums)
        res = 0
        
        while r < n-1:
            farthest = 0
            for i in range(l,r+1):
				# calculate the farthest distance can be made inside the window
                farthest = max(farthest, i+nums[i])
			# shift the pointers to the new window
            l = r + 1
            r = farthest
            res += 1
        return res