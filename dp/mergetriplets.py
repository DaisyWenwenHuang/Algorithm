# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/
# leetcode 1899
#  medium
# greedy
# using zip to avoid two loops 
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        t = [0,0,0]
        
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1]>target[1] or triplet[2]>target[2]:
                continue
            for i in range(3):
                t[i] = max(t[i],triplet[i])
        
        for i in range(3):
            if target[i] != t[i]:
                return False
        return True
                