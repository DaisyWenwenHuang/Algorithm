# https://leetcode.com/problems/maximum-product-subarray/
# leetcode 152
# medium 
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums) 
        curmin,curmax=1,1
        
        for n in nums:
            if n==0:
                curmin,curmax=1,1
                continue
            temp=curmax*n
            curmax=max(curmax*n,curmin*n,n) # curmax could be one of the three
            curmin=min(curmin*n,temp,n) # curmin could be one of the three, here using
                                            # temp because curmax could be changed due to 
                                            # above code
            res=max(res,curmax)
        return res
    
