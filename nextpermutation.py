# https://leetcode.com/problems/next-permutation/
# find the next permutation that is the next greater integer than the input list integer.
# loop from the end of the list, comepair to the ele in the front. 

# BF
# list all the permutations and sort to find the next greater one.
# but, time O(n!) and space are not efficient 
class Solution:

	# swap function 
    def swap(self, nums, ind_1, ind_2):
        nums[ind_1], nums[ind_2] = nums[ind_2], nums[ind_1]
    
    # reverse the sequence of an array
    def reverse(self, nums, start, end):
        while start < end:
            self.swap(nums, start, end)
            start += 1
            end -= 1
			
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
		# corner case
        if len(nums) == 1:
            return 
		# corner case
        if len(nums) == 2:
            return self.swap(nums, 0, 1)
		# iterate from the right to left to find the pivot point where ascending becomes to descending
        dec_ind= len(nums) - 2
        while dec_ind >= 0 and nums[dec_ind] >= nums[dec_ind + 1]:
            dec_ind -= 1
		# reverse the sequence of the array stars from the right of the pivot point
        self.reverse(nums,dec_ind+1,len(nums)-1)
		# out of bound: the array is a natural ascending array
		# return its reversed version
        if dec_ind == -1:
            return
		# first point right of the pivot point
        next_num = dec_ind + 1
		# iterate from the next_num point to the end of the array to find the next greater point where the number of that point is greater than the pivot point number. note the sequence is already sorted here.
        while next_num < len(nums)  and nums[next_num] <= nums[dec_ind]:
            next_num += 1
		# swap the pivot point and the next_num point
        self.swap(nums, next_num, dec_ind)