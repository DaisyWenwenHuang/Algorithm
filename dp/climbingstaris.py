# https://leetcode.com/problems/climbing-stairs/
# leetcode 70
# easy

class Solution:
    def climbStairs(self, n: int) -> int:
        f1 = 1
        f2 = 1
        f = 0
        if n <= 1:
            return 1
        for i in range(n-2,-1,-1):
            f = f1 + f2
            f2 = f1
            f1 = f
        return f
            