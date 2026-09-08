class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dico  = {}

        for i in range(len(nums)):
            if nums[i] in dico:
                dico[nums[i]] +=1
            else: 
                dico[nums[i]] = 1

        
        for val in dico.values():
            if val > 1:
                return True

        return False