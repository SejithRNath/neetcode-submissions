class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mem = {len(s):True}
        def dfs(i):
            if i==len(s):
                return True
            if i in mem:
                return mem[i]
            for k in wordDict:
                if (i + len(k)) <= len(s) and k == s[i:i+len(k)]:
                    
                    if dfs(i+len(k)):
                        mem[i]=True
                        return True
            mem[i]=False
            return False
            
        return dfs(0)
