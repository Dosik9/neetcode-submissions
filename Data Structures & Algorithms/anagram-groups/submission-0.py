class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_hash = {}

        for s in strs:
            s_sorted = "".join(sorted(s))
            if s_sorted not in strs_hash:
                strs_hash[s_sorted] = []
            
            strs_hash[s_sorted] += [s]     
        
        return list(strs_hash.values())
            