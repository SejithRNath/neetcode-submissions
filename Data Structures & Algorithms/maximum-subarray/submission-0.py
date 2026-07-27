class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = min(nums)
        for i in range(len(nums)):
            s = 0
            for j in range(i,len(nums)):
                s += nums[j]
                res = max(s, res)
        return res

        