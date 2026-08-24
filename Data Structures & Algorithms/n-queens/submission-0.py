class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=set()
        posdig=set()
        negdig=set()
        board=[["."]*n for _ in range(n)]
        res=[]
        def dfs(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return 
            for c in range(n):
                if c in col or (r+c) in posdig or (r-c) in negdig:
                    continue
                board[r][c] ="Q"
                col.add(c)
                posdig.add(r+c)
                negdig.add(r-c)
                dfs(r+1)
                board[r][c] ="."
                col.remove(c)
                posdig.remove(r+c)
                negdig.remove(r-c)

        dfs(0)
        return res
