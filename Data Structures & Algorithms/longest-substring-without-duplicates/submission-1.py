class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        part = ""
        
        for c in s:
            if c in part:
                part = part[part.index(c) + 1:]
                
            part += c
            longest = max(longest, len(part))
        
        return longest