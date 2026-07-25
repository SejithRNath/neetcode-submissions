class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr =[(p,s)for p,s in zip(position,speed) ]
        stack =[]
        arr.sort( reverse = True)
        # print(arr)
        for p,s in arr:
            stack.append((p,s))
            if len(stack)==1:
                continue
            else:
                a,b= stack[-1]
                # print(a,b)
                c,d=stack[-2]
                # print(c,d)
                if (target-a)/b <= (target -c)/d:
                    stack.pop()
        return len(stack)
