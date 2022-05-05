# https://leetcode.com/problems/palindrome-partitioning/
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        par = []
              
        def dsf(i):
            if i >= len(s):
                res.append(par.copy())
                return
            for j in range(i,len(s)):
                if self.valid(s,i,j):
                    par.append(s[i:j+1])
                    dsf(j+1)
                    par.pop()
        dsf(0)
        return res
        
    def valid(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l,r = l + 1,r - 1
        return True