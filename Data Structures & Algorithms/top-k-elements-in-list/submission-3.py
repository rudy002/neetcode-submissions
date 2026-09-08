class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        
        for num in nums: 
            count[num] = count.get(num, 0) + 1

        frequence = [[] for i in range(len(nums) + 1)]

        for key, v in count.items():
            frequence[v].append(key)

        res = []

        for i in range(len(frequence)-1, 0, -1):
            for n in frequence[i]:
                res.append(n)
            if len(res) == k:
                return res
