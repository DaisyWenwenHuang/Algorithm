# https://leetcode.com/problems/longest-palindromic-substring/
# leetcode 5
# medium
# 1-d dp
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        size = 0
        for i in range(len(s)):
			# odd length 'abac'--> 'aba'
            left, right = i,i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > size:
                    res = s[left:right+1]
                    size = right-left+1
                left -= 1
                right += 1

			# even lenght "abbc" --> 'bb'
            left,right = i,i+1
            while left >=0 and right<len(s) and s[left]==s[right]:
                if (right-left+1) > size:
                    res = s[left:right+1]
                    size = right-left+1
                left -= 1
                right += 1

        return res
