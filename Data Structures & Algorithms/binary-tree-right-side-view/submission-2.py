# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
             return []
        queue = []
        res=[]
        queue.append(root)
        while queue:
            q =len(queue)
            for i in range(q):
                node = queue.pop(0)
                if i+1 == q:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res
        # if not root:
        #     return []
            
        # queue = [root]
        # res = []
        
        # while queue:
        #     q = len(queue)
        #     for i in range(q):
        #         node = queue.pop(0)
                
        #         # If it's the last node in this level, add to result
        #         if i + 1 == q:
        #             res.append(node.val)
                
        #         # Only add actual nodes to the queue
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
                    
        # return res
