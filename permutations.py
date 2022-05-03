# https://leetcode.com/problems/permutations/
Class Solution:
	def permute(self,nums):
		res = []

		# base case
		if len(nums) == 1:
			# result is a list of list
			return [nums[:]]

		for i in range(len(nums)):
			n = nums.pop(0)

			perms = self.permute(nums)
			for perm in perms:
				perm.append(n)
			res.extend(perms)
			nums.append(n)
	return res