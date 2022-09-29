# https://leetcode.com/problems/partition-labels/
# leetcode 763
# medium
# greedy
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counts = {}
		# dictionary to store each elemnt's last appear index
        for index,ele in enumerate(s):
            counts[ele] = index
        res = []
        size = 0
        end = 0
        for index, ele in enumerate(s):
            size += 1
            end = max(end, counts[ele])
            if index  == end:
                res.append(size)
                size = 0
        return res