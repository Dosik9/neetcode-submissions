class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        hashmap = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hashmap:
                answer=[hashmap[difference], i]
            else:
                hashmap[nums[i]] = i
        
        return answer          