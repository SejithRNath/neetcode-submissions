# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.res = None
    
        def dfs(node):
        # Stop if node is null OR if we already found the answer
            if not node or self.res is not None:
                return 
            
            # 1. Go Left
            dfs(node.left)
            
            # 2. Process Node
            self.k -= 1
            if self.k == 0:
                self.res = node.val
                return  # Found it! Stop processing this branch.
            
            # 3. Go Right
            dfs(node.right)
            
        dfs(root)
        return self.res