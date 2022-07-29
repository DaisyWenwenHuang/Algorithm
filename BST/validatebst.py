# https://leetcode.com/problems/validate-binary-search-tree/
# leetcode 98_medium
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        def isValid(node, left, right):
			# helper function to do recursive call 
            if not node:
                return True
            if not (node.val<right and node.val > left):
                return False
            
            return ((isValid(node.left,left,node.val)) and (isValid(node.right,node.val,right)))
        
        
        return isValid(root,float('-inf'),float('inf'))