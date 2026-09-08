class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        
        for num in nums: 
            count[num] = count.get(num, 0) + 1

        res = []
        for _ in range(k):
            best = max(count, key = count.get)
            res.append(best)
            del(count[best])
    
        return res