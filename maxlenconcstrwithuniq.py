# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
# backtracking
class Solution:
    def maxLength(self, arr: List[str]) -> int:      
        charset = set()
        
        def notvalid(charset,s):
            c = Counter(charset) + Counter(s)
            return max(c.values()) > 1
			# prev = set()
			# for c in s:
			# 	if c in charset or c in prev:
			# 		return True
			# 	prev.add(c)
			# return False 

        def backtrack(i):
            # base case
            if i == len(arr):
                return len(charset)

            res = 0
            # desicion that concatenate the arr[i]
            if not notvalid(charset,arr[i]):
                for c in arr[i]:
                    charset.add(c)
                res = backtrack(i + 1)
                # clean up
                for c in arr[i]:
                    charset.remove(c)
            # desicion that do not concatenate the arr[i]
            not_incld = backtrack(i+1)
            return max(res,not_incld)

        
        return backtrack(0)
            