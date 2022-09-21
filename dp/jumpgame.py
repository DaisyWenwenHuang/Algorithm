# https://leetcode.com/problems/jump-game/
# leetcode 55
# medium
# greedy
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # from the  end to the beginning
		flag = len(nums)-1
        
        for i in range(len(nums)-1,-1,-1):
			# keep moving the flag
            if i + nums[i] >= flag:
                flag = i
        if flag == 0:
            return True
        else:
            return False