# https://leetcode.com/problems/palindromic-substrings/
# leetcode 647
# medium 
# 1-D dp
class Solution:
    def countSubstrings(self, s: str) -> int:
        # each element can be its own palindrom 
		res = len(s)
        for i in range(len(s)):
            # odd 
			# odd length of the palindrom
            left  = i-1
            right = i+1
            while left >= 0 and right < len(s) and s[left]==s[right]:
                res += 1
                left -= 1
                right += 1
            
            # even 
			# even length of the palindrom
            left = i
            right = i+1
            while left >=0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -=1
                right += 1
        return res
	