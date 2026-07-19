class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp=[]
        res=[]
        temp= nums[::]
        for i in range(len(nums)):
            value=temp[i]
            temp[i]=1
            res.append(math.prod(temp))
            temp[i]=value
        return res


        