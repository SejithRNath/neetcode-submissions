class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        res=[]
        count=1
        next=nums[0]
        for i in range(1,len(nums)):
           
            if nums[i]-nums[i-1]== 1 :

                count+=1
            elif nums[i]-nums[i-1]==0:
                continue
            else:
                res.append(count)
                count=1
        res.append(count)
        return max(res)


        
        