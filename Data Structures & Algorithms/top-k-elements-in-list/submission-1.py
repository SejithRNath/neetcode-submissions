class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = defaultdict(int)
        r = []
        res= []
        for i in nums:
            h[i] = 1+h.get(i,0)
        for _ in range(k):
            m = 0
            key = None
            for i,j in h.items():
                if j > m and i not in r:
                    m = j
                    key = i
                    
            if key is not None:
                res.append(key)
                r.append(key)
        print(res)
        return res