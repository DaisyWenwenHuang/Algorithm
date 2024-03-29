# https://leetcode.com/problems/gas-station/
# leetcode 134
# medium
# greedy
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [(i-j) for i,j in zip(gas,cost)]
        if sum(diff) < 0:
			# no solution
            return -1
        else:
			# has a unique solution
            total = 0
            start = 0
            for k in range(len(diff)):
                total += diff[k]
                if total < 0:
                    total = 0
                    start = k + 1
            return start