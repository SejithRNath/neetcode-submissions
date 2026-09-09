class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # minval = 0
        minval = 1
        maxval = 1
        
        res = nums[0]
        for i in nums:
            cur=maxval*i
            maxval = max(minval*i,maxval*i,i)
            minval = min(minval*i,cur,i)
            res = max(res,maxval)
        return res

        