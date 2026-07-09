class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0 
        high = len(nums)-1
        res = nums[0]
        if nums[low]<nums[high]:

            # res =min(nums[low],res)
            # break
            return nums[low]
        while low <= high:
            # if nums[low]<nums[high]:
            #     res =min(nums[low],res)
            #     break
            mid =  (low+high)//2
            res =min(nums[mid],res)
            if nums[mid]>nums[high]:
                low = mid +1
            else:
                high = mid -1
        return res
        