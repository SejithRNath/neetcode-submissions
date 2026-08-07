class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: return ""
        
        count_t = Counter(t)
        required = len(t)
        
        l = 0
        min_len = float("inf")
        min_window = ""
        
        for r in range(len(s)):
            # Expand the window by adding s[r]
            if count_t[s[r]] > 0:
                required -= 1
            count_t[s[r]] -= 1 
            
            # When window is valid, try to shrink it from the left
            while required == 0:
                # Update minimum window if this one is smaller
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    min_window = s[l:r+1]
                
                # Remove s[l] from the window
                count_t[s[l]] += 1
                if count_t[s[l]] > 0:
                    required += 1
                l += 1
                
        return min_window
        