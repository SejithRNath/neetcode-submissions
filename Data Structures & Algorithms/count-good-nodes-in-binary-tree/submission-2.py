# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        value = root.val
        self.count=0
        def treetrav(root,value):
            if not root:
                
                return 
            if root.val >=value :
                self.count+=1
                value = root.val
            treetrav(root.left,value)  
            treetrav(root.right,value)
        treetrav(root.left,value)
        
        treetrav(root.right,value)
        return self.count+1


        