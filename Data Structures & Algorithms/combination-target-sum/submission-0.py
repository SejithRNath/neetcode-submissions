class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        def dfs(i,total,sub):
            if total == target :
                res.append(sub.copy())
                return
            if i >= len(nums) or total > target:
                return
            sub.append(nums[i])
            dfs(i,total+nums[i],sub)
            
            sub.pop()
            dfs(i+1,total,sub)
        dfs(0,0,sub)
        return res



        