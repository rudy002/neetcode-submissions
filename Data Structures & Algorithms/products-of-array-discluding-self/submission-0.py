class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [1] * len(nums)

        prefix = 1
        sufix = 1

        for i in range(len(nums)):
            result[i] = prefix 
            prefix = prefix * nums[i]
        
        for i in range(len(nums) -1, -1, -1):
            result[i] = result[i] * sufix
            sufix = sufix * nums[i]
        
        return result 