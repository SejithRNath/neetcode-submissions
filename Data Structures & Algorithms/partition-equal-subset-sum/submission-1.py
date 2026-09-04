class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2!=0:
            return False
        n =len(nums)
        target = total//2
        mem=[[-1]*(target+1) for _ in range(n+1)]

        def dfs(i,target):
            
            if target == 0:
                return 1

        
            if i >= n or target < 0:
                return 0
            
            if mem[i][target] != -1:
                return mem[i][target]
            
            mem[i][target] = (dfs(i+1,target) or dfs(i+1,target-nums[i]))

            return mem[i][target]
        return bool(dfs(0,target))                

        