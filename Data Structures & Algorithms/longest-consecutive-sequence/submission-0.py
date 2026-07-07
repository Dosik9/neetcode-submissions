class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for n in nums_set:
            if n-1 in nums_set:
                continue
            
            current_len = 1
            while (n + current_len) in nums_set:
                current_len +=1
            
            if current_len > longest:
                longest = current_len
        
        return longest