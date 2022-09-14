# https://leetcode.com/problems/climbing-stairs/
# leetcode 70
# easy
# dp solution, bottom-up
class Solution:
    def climbStairs(self, n: int) -> int:
		# only need two memeroy to store the last two value calculated
		# f(3) = f(1)+f(2)
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

# better code
class Solution:
    def climbStairs(self, n: int) -> int:
		one,two = 1,1
		for i in range(n-1):
			temp = one
			one = one + two
			two = temp
		return one 