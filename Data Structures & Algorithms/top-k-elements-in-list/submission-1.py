class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        
        result = [k for k,v in sorted(d.items(), key=lambda x: x[1], reverse=True)]
        return result[:k]
