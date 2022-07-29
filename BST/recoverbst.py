# https://leetcode.com/problems/recover-binary-search-tree/
# leetcode 99 _medium
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # inorder traverse the tree and get a list (suppose to be sorted if it is a valid bst)
        # find the two numbers that are not in order in the list
        # traverse the tree again and swape the two displaced number
        # this will using spcae O(n)

		# but the input is a list 