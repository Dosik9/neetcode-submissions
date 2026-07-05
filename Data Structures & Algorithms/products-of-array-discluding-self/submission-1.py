class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        prefix, suffix = 1, 1
        j = len(nums)
        for i in range(len(nums)):
            j -= 1
            output[i] *= prefix
            output[j] *= suffix
            prefix *= nums[i]
            suffix *= nums[j]
        
        return output