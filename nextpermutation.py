# https://leetcode.com/problems/next-permutation/
# find the next permutation that is the next greater integer than the input list integer.
# loop from the end of the list, comepair to the ele in the front. 

# BF
# list all the permutations and sort to find the next greater one.
# but, time O(n!) and space are not efficient 
nums=[1,2,3]
pivit = -1

for i in range(len(nums)-1, 0,-1):
	print(i)
	if nums[i] <= nums[i-1]:
		continue
	else:
		pivit = nums[i-1]
		k = len(nums)-1
		print(pivit)
		print(f'k ={k}')
		while k>=i:
			print('inside while')
			print(k)
			if nums[k]> pivit:
				print('*')
				print(nums[k])
				print(nums[i-1])
				nums[k],nums[i-1] = nums[i-1],nums[k]
				print('**')
				print(nums[k])
				print(nums[i-1])					
				break

		# 		print(nums[i:])
		# 		nums[i:].reverse()
		# 		print(nums[i:])

# if pivit == -1:
# 	nums.reverse()

print(nums)