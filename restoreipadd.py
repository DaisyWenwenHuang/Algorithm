# https://leetcode.com/problems/restore-ip-addresses/
# backtracking
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # edge cases
        if len(s) < 4 or len(s) > 12:
            return []
        
        def Isvalid(str):
            if str[0] == '0' and len(str) != 1:
                return False
            if int(str) <= 255:
                return True
        
        res = []
        ip = []
        def backtrack(i,dots,curip):
            # base case
            if dots == 4 and i == len(s):
                res.append(curip[:-1])
            
            if dots > 4:
                return
            
            for j in range(i, min(i+3,len(s))):
                if Isvalid(s[i:j+1]):
                    backtrack(j+1,dots+1,curip + s[i:j+1]+'.')
                else:
                    return
        backtrack(0,0,'')
        return res
                
                