class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem=defaultdict(int)
        def dfs(amount):
            if amount==0:
                return 0
            
            if amount<0:
                return float("inf")

            if amount in mem:
                return mem[amount]
            res=float("inf")
            for i in coins:
                if amount-i>=0:

                    res=min(res,1+dfs(amount-i))
            mem[amount] = res
            return res
        ans=dfs(amount)
        if ans == float("inf"):
            return -1
        return ans
