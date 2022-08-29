# https://leetcode.com/problems/longest-common-subsequence/
# leetcode 1143
# medium
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp_grid = [[0 for i in range(n+1)] for j in range(m+1)]
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if text1[i] == text2[j]:
                    dp_grid[i][j] = 1 + dp_grid[i+1][j+1]
                else:
                    dp_grid[i][j] = max(dp_grid[i][j+1],dp_grid[i+1][j])
        return dp_grid[0][0]