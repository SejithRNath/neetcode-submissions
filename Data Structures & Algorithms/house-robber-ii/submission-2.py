class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            dp=[0]*len(nums)
            dp[0]=nums[0]
            if len(nums) == 1:
                return nums[0]
            dp[1]=max(nums[0],nums[1])
            for i in range(2,len(nums)):
                # if i == len(nums)-1:
                #     dp[i]=max(dp[i-2],dp[i-1])
                # else:
                    dp[i]=max(dp[i-2]+nums[i],dp[i-1])
            return dp[len(nums)-1]
        if len(nums)==1:
            return nums[0]
        return max(helper(nums[1:]),helper(nums[0:len(nums)-1]))        
        