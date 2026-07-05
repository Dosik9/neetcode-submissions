class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        
        nums_hash = {}
        
        for i in range(len(nums)):
            answer = 1
            for j in range(len(nums)):
                if i == j: 
                    continue
                answer *= nums[j]
            output.append(answer)
        
        return output