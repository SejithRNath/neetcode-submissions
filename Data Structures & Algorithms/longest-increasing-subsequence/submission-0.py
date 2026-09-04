class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mem={}
        def dfs(i):
            if i == len(nums):
                mem[i]=1
                return mem[i]
            
            if i in mem:
                return mem[i]
            res=1
            for k in range(i+1,len(nums)):
                if nums[i] < nums[k]:
                    res = max(res,1+dfs(k))
            mem[i]=res
            return res
        return max(dfs(i) for i in range(len(nums)))