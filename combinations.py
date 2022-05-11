# https://leetcode.com/problems/combinations/
# backtracking
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
                

        def dfs(start,cur):
            # base case
            if len(cur) == k :
                res.append(cur.copy())
                return
            
            for i in range(start,n + 1):
                cur.append(i)
                dfs(i+1, cur)
            
                cur.pop()
            
        dfs(1,[])
        return res