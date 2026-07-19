class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1

        while r>l:

            while l<r and not self.alphanum(s[l]):
                l +=1
            while r>l and not self.alphanum(s[r]):
                r -=1
            if s[l].lower() != s[r].lower():
                return False
            l +=1
            r -=1
        return True
    
    def alphanum(self,s):
        return (ord("A")<=ord(s)<=ord("Z")or
                ord("a")<=ord(s)<=ord("z")or 
                ord("0")<=ord(s)<=ord("9"))

        