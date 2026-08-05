# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # res=[]
        # les=[]
        # def dfs(root,c,val):
        #     if root.value == c:
        #         return root
        #     if not root:
        #         return 0
        #     left = dfs(root.left,c,val)
        #     right = dfs(root.right,c,val)
        #     if left:
        #         val.append(left)
        #     if right:
        #         val.append(right)
        # dfs(root,p,res)
        # dfs(root,q,les)
        if not root or root == p or root == q:
            return root
        
        # Search left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both sides found a target, this root is the LCA
        if left and right:
            return root
            
        # Otherwise, return the side that found a target
        return left or right
            
        