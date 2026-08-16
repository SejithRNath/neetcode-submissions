class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return [[]]
        
        perm = self.permute(nums[1:])
        new = []
        for p in perm:
            
            for i in range(len(p)+1):
                pcpy = p.copy()
                pcpy.insert(i,nums[0])
                new.append(pcpy)
            
        
        return new

        
        