# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
def bisearch(self,nums,target,start,end):
        mid = (start + end)//2
        if nums[mid] == target:
            # left one by one
            lp = mid
            while lp >= 0 and nums[lp] == target:
                lp -= 1
            # right one by one
            rp = mid
            while rp < len(nums) and nums[rp] == target:
                rp += 1
            return nums[lp:rp+1]
        if nums[mid] > target:
            # left bisearch
            bisearch(nums,target,start,mid)
        if nums[mid] < target:
            # right bisearch
            bisearch(nums,target,mid,end)