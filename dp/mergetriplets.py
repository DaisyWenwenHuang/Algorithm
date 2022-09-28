# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/
# leetcode 1899
#  medium
# greedy
# using zip to avoid two loops 
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        for triplet in triplets:
            [x-y for x, y in zip(triplet,target)]