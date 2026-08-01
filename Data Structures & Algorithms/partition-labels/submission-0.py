class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count={}
        for i in range(len(s)):
            count[s[i]] = i
        
        end =0
        res= []
        size = 1
        for j in range(len(s)):
            end = max(count[s[j]],end)
            if end == j:
                res.append(size)
                size = 1
            else:
                size+=1
        return res
        
                
