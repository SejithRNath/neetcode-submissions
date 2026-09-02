class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(i):
            if sum(l)==target:
                res.append(l.copy())
                return
            if sum(l)>target or i>=len(nums):
                return
            
            l.append(nums[i])
            dfs(i)

            l.pop()

            dfs(i+1)  
        l=[]
        dfs(0)
        return res  
        