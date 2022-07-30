# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# leetcode 104 easy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# solution 1 dfs
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # dfs
        def dfs(root):
            if not root:
                return 0

            return 1 + max(dfs(root.left),dfs(root.right))
        return dfs(root)



# solution 2 bfs


class Solution:
	
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level

		
# solution 3 iteration 
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root,1]]
        res = 0
        while stack:
            node,depth = stack.pop()
            if node:
                stack.append([node.left,depth+1])
                stack.append([node.right,depth+1])
                res = max(res,depth)
        return res