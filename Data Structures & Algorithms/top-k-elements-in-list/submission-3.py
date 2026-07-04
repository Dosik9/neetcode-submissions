class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n_count = {}
        answer = []
        for n in set(nums):
            n_count[n] = nums.count(n)
        
        n_k = n_count.keys()
        n_v_s = sorted(n_count.values())[-k:]

        for n in n_k:
            if n_count[n] in n_v_s:
                answer.append(n)
        
        return answer