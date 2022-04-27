# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# binary search (a bit twisted)
class Solution:
	def searchRange(self, nums: List[int], target: int) -> List[int]:
		# corner case
		if len(nums) == 0:
		    return [-1,-1]
		left = self.binsearch(nums,target,True)
		right = self.binsearch(nums,target,False)
		return [left, right]

	# leftbias [True/False], if false, res is rightbiased
	def binsearch(self, nums,target,leftbias):
		l,r = 0, len(nums) - 1
		i = -1

		while l <= r:
			m = (l + r) // 2
			if target > nums[m]:
				l = m + 1
			elif target < nums[m]:
				r = m - 1
			else:
				i = m
				if leftbias:
					r = m - 1
				else:
					l = m +	1
		return i
		