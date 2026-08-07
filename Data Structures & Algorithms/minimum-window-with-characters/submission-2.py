class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t =="":
            return ""
        h = Counter(t)
        window = {}
        have = 0
        need = len(h)        
        res = [-1,-1]
        reslen = float("inf")
        l = 0
        for r in range(len(s)):
            c = s[r]
            if c in h:
                window[c] = window.get(c,0)+1
                if window[c] == h[c]:
                    have+=1
                while have == need:
                    if (r-l+1)<reslen:
                        res[0] = l
                        res[1] = r+1
                        reslen = r - l +1
                    a = s[l]
                    if a in h:
                        window[a] -=1
                        if window[a]<h[a]:
                            have-=1
                    l+=1
        l,r = res
        return s[res[0]:res[1]] if reslen != float("inf") else ""
                    



