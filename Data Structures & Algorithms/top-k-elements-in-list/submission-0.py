class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=defaultdict(list)
        
        for i in nums:
            res[i].append(i)

        res_sort=dict(sorted(res.items(),key=lambda item: len(item[1]),reverse=True))
        first_k=dict(list(res_sort.items())[:k])
        return list(first_k.keys())