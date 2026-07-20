class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        stack = []
        max_c=1
        for i in s:
            if i in stack:
                max_c = max(len(stack),max_c)
                while i in stack:
                    stack.pop(0)
                stack.append(i)
                
                

            else:
                stack.append(i)
        max_c = max(len(stack),max_c)
        return max_c
        