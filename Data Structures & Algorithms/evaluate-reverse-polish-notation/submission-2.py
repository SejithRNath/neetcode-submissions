class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        sum = 0
        stack =[]
        for i in tokens:
            if i == "+":
                b = int(stack[-1])
                stack.pop()

                a = int(stack[-1])
                stack.pop()
                stack.append(a+b)
            elif i == "-":
                b = int(stack[-1])
                stack.pop()

                a = int(stack[-1])
                stack.pop()
                stack.append(a-b)
            elif i == "*":
                b = int(stack[-1])
                stack.pop()

                a = int(stack[-1])
                stack.pop()
                stack.append(a*b)
            elif i == "/":
                b = int(stack[-1])
                stack.pop()

                a = int(stack[-1])
                stack.pop()
                stack.append(a/b)
            else:
                
                    stack.append(i)
               
                    

                
        return int(stack[-1])