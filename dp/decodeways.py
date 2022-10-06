# https://leetcode.com/problems/decode-ways/
# leetcode 91 
# medium
# 1-d dp
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0]*len(s)
        for i in range(len(s)-1,-1,-1):
            # encounter 0
            if s[i] == 0