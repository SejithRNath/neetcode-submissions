class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ball = 0
        gp =len(nums)-1
        for i in range(len(nums)-2,-1,-1):
        
            if i+nums[i] >= gp:
                gp = i
            
        if gp == ball:
            return True
        else:
            return False
            


        
        
        