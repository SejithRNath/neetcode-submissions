class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        cost =0
        while l<len(prices) and r<len(prices):
            if prices[r]<prices[l]:
                l=r
                r+=1
            else:
                cost=max(cost,(prices[r]-prices[l]))
                r+=1
        return cost


        