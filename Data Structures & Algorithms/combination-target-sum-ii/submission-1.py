class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # res= set()
        res= []
        candidates.sort()
        # h= defaultdict(int)
        # for j in candidates:
        #     h[j]=h.get(j,0)+1
        def dfs(i,cur,total):
            if total == target:
                # res.add(tuple(cur.copy()))
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            # if h[candidates[i]]:
            #     cur.append(candidates[i])
            #     h[candidates[i]] -=1
            cur.append(candidates[i])
            dfs(i+1,cur,total+candidates[i])
            cur.pop()
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i +=1
            dfs(i+1,cur,total)
        dfs(0,[],0)
        return res
        