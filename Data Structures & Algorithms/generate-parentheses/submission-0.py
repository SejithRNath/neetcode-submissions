class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        stack=[]
        def dfs(op,close,stack):
            if op == close == n:
                res.append("".join(stack))
                return

            if op <n:
                stack.append("(")
                dfs(op+1,close,stack)
                stack.pop()
            if close <op:
                stack.append(")")
                dfs(op,close+1,stack)
                stack.pop()
        dfs(0,0,stack)

        return res
            
        