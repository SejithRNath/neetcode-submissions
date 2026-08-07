class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        h=Counter(s1)
        for i in range(len(s2)):
            if s2[i] in s1:
                res={}
                k = i 
                while k<len(s2):
                    if s2[k] not in s1:
                        break
                    res[s2[k]] = res.get(s2[k],0) + 1
                    if res[s2[k]] > h[s2[k]]:
                        break
                    if res == h:
                        return True
                    k+=1
        return False
        