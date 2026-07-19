class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False
    
        b = list(t)
        for i in s:
            if i in b:
                
                b.remove(i)
            
        if len(b)!=0:
            return False
        else:
            return True
            

        