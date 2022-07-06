# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# depth search first
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno',
                 '7':'pqrs','8':'tuv','9':'wxyz'}
        res = []

        def dsf(i,curstr):
            if len(curstr) == len(digits):
                res.append(curstr)
                return
            
            for char in phone[digits[i]]:
                dsf(i + 1,curstr + char)
		# code below to make sure if the digits is empty, we return [], not ['']
        if digits:
            dsf(0,'')
        return res