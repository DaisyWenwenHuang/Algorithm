# https://leetcode.com/problems/valid-parenthesis-string/
# leetcode 678
# medium
# greedy
class Solution:
    def checkValidString(self, s: str) -> bool:
        leftmax,leftmin = 0,0
        for ele in s:
            if ele == '(':
                leftmax += 1
                leftmin += 1
            elif ele == ")":
                leftmax -= 1
                leftmin -= 1
            else:
                leftmax += 1
                leftmin -= 1
            if leftmax < 0:
                return False
            if leftmin < 0:
                leftmin = 0
        return leftmin == 0