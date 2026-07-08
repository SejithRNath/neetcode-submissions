class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ma = 0
        n=len(heights)
        
        for i in range(len(heights)):
            left,right=-1,n
            j=i-1
            k=i+1
            ma=max(ma,heights[i])
            #print(j)
            while j>=0:
                if heights[j]<heights[i]:
                    left = j
                    break
                j-=1
            #print(k)
            while k<n:
                if heights[k]<heights[i]:
                    right = k
                    break
                else:
                    k+=1
                    #print(k)  
            area = (right-left-1)*heights[i]
            print(area)
            ma = max(ma,area) 
        return ma

# class Solution:
#     def largestRectangleArea(self, heights: list[int]) -> int:
#         ma = 0
#         n = len(heights)
        
#         for i in range(n):
#             # 1. FIX: Default to extreme boundaries if no smaller bar is found
#             left = -1
#             right = n
            
#             j = i - 1
#             k = i + 1
            
#             while j >= 0:
#                 if heights[j] < heights[i]:
#                     left = j
#                     break
#                 j -= 1
                
#             while k < n:
#                 if heights[k] < heights[i]:
#                     right = k
#                     break
#                 k += 1 
                    
#             # 2. FIX: Width is the space strictly between 'left' and 'right'
#             area = (right - left - 1) * heights[i]
#             ma = max(ma, area) 
            
#         return ma
        