class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        h = dict()
        d = dict()
        for i in range(len(s)):
            h[s[i]] = 1+h.get(s[i],0)
            d[t[i]] = 1+d.get(t[i],0)
        
   
           
        
        return h == d

